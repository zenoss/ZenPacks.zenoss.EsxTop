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

import os

from Products.ZenRRD.tests.BaseParsersTestCase import BaseParsersTestCase

from ZenPacks.zenoss.EsxTop.parsers.esx.esxtop import esxtop


class EsxTopParsersTestCase(BaseParsersTestCase):

    def testLinuxParsers(self):
        """
        Test all of the parsers that have test data files in the data
        directory.
        """
        datadir = "%s/parserdata/esx" % os.path.dirname(__file__)
        
        parserMap = {
             "check_esxtop --statCategory='Group Cpu' --component=host": esxtop,
             "check_esxtop --statCategory='Memory'": esxtop,
        }
        
        self._testParsers(datadir, parserMap)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(EsxTopParsersTestCase))
    return suite

