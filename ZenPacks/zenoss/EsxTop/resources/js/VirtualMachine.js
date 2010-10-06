/*
###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################
*/

(function(){

var ZC = Ext.ns('Zenoss.component');

var ZEvActions = Zenoss.events.EventPanelToolbarActions;

ZC.VirtualMachinePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            autoExpandColumn: 'name',
            componentType: 'VirtualMachine',
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{ 
                id: 'name',
                dataIndex: 'name',
                header: _t('VM Name'),
                width: 160
            }]
        });
        ZC.VirtualMachinePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('VirtualMachinePanel', ZC.VirtualMachinePanel);
ZC.registerName('VirtualMachine', _t('Virtual Machine'), _t('Virtual Machines'));

})();

