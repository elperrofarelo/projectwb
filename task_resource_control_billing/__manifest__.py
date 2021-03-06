# -*- coding: utf-8 -*-
# Copyright 2016 Jarsa Sistemas S.A. de C.V.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Resource Control Billing',
    'summary': 'Resource control Billing',
    'version': '11.0.1.0.0',
    'category': 'Project',
    'author': (
        'Jarsa sistemas S.A de C.V. ,'
        'Odoo Community Association (OCA)'),
    'website': 'https://www.odoo-community.org',
    'license': 'LGPL-3',
    'depends': [
        'task_resource_control',
        'analytic_billing_plan',
        ],

    'data': [
        'wizards/resource_control.xml',
        'wizards/billing_request_view.xml',
    ],
    'installable': True,
}
