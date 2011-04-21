###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010 Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/#
###########################################################################

from zope.interface import implements

from Products.Zuul.infos.component import ComponentInfo

from ZenPacks.zenoss.EsxTop.interfaces import *

class VirtualMachineInfo(ComponentInfo):
    implements(IVirtualMachineInfo)

    @property
    def monitored(self):
        return False

    @property
    def status(self):
        return 'Up'

