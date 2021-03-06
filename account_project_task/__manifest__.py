# -*- coding: utf-8 -*-
# Copyright 2015 Eficent Business and IT Consulting Services S.L.
# Copyright 2016 Jarsa Sistemas S.A. de C.V.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": 'Accounting with Project Task dimension',
    "summary": "Introduces Project Task in account move lines",
    "version": "11.0.1.0.0",
    "author": "Eficent Business and IT Consulting Services S.L., "
              "Odoo Community Association (OCA), Jarsa Sistemas S.A. de C.V.",
    "description": "Module to assign the project to the move line",
    "website": "http://www.eficent.com",
    "category": "Accounting & Finance",
    "depends": ['account_project'],
    "license": "AGPL-3",
    "data": [
        "views/account_move_view.xml",
    ],
    "installable": True,
}
