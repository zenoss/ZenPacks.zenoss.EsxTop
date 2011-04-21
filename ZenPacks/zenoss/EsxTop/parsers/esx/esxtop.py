###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010 Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

__doc__ = """esxtop

Parse the output of the check_esxtop command and populate the datapoints
with data from the output.
"""
import logging
log = logging.getLogger('zen.esxtop.parser')

from Products.ZenUtils.Utils import prepId
from Products.ZenRRD.CommandParser import CommandParser


class esxtop(CommandParser):
    def _parseOutput(self, output):
        """
        Output from the command has the format

        name\tvalue
        """
        points = {} 
        for line in output.strip().splitlines():
            if not line.strip():
                continue
            words = line.rsplit('\t',1)
            dp = prepId( words[0] )
            value = float(words[1])
            points.update({dp:value})
        return points
    
    def processResults(self, cmd, result):
        """
        Process the output and send events on error.
        """
        output = cmd.result.output
        exitCode = getattr(cmd.result, 'exitCode', 0)
        if exitCode != 0 or \
           output.startswith('ERROR: '):
            msg = output if output else "Unknown error"
            evt = dict(
                       device=cmd.deviceConfig.device,
                       summary=msg,
                       severity=cmd.severity,
                       eventKey=cmd.eventKey,
                       eventClass=cmd.eventClass,
                       component=cmd.component)
            result.events.append(evt)
            return result

        if not output:
            log.error("No output for parser")
            return result

        valueMap = self._parseOutput(output)
        for dp in cmd.points:
            value = valueMap.get(dp.id)
            if value is not None:
                result.values.append( (dp, value) )
        return result
