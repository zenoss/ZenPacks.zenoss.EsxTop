###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010 Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

__doc__ = """esxtop

Modeler plugin that adds basic VM components to VirtualHostMonitor hosts.
"""

import logging
import os

from Products.DataCollector.plugins.CollectorPlugin import PythonPlugin
from Products.ZenUtils.Utils import zenPath, prepId
from twisted.internet.utils import getProcessOutput


class esxtop(PythonPlugin):
    relname = 'guestDevices'
    modname = 'ZenPacks.zenoss.ZenossVirtualHostMonitor.VirtualMachine'

    deviceProperties = PythonPlugin.deviceProperties + (
        'zCommandUsername',
        'zCommandPassword',
    )

    def findPath(self):
        path = []
        for p in __file__.split(os.sep):
            if p == 'modeler': break
            path.append(p)
        return os.sep.join(path)

    def collect(self, device, log):
        path = self.findPath()
        log.info("Running esxtop modeler plugin")
        cmd = path + '/libexec/check_esxtop'
        py = zenPath("bin", "python")
        args = [cmd,
                '--server=%s' % device.id,
                '--user=%s' % device.zCommandUsername,
                '--showvms',
        ]
        os.environ['VI_PASSWORD'] = device.zCommandPassword
        return getProcessOutput(py, args, os.environ)

    def process(self, device, results, log):
        if results.startswith('Bad hostname') or \
           results.startswith('Login failed') or \
           results.startswith('ERROR') or \
           'command not found' in results:
            log.error(results)
            return None

        rm = self.relMap()
        for vm in results.split('\n'):
            info = {}
            id = prepId(vm)
            if not id: # Toss out blank lines
                continue
            info['id'] = prepId(vm)
            info['displayName'] = vm
            info['adminStatus'] = True # We don't monitor actual status
            info['operStatus'] = True # We don't monitor actual status
            om = self.objectMap(info)
            rm.append(om)

        return rm

