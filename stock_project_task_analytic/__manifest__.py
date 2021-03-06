# -*- coding: utf-8 -*-
# 2015 Eficent Business and IT Consulting Services S.L.
# Copyright 2016 Jarsa Sistemas S.A. de C.V.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "Stock Project Task",
    "summary": "Adds an project task in stock move",
    "version": "11.0.1.0.0",
    "author": "Eficent Business and IT Consulting Services S.L.,"
    "Odoo Community Association (OCA), Jarsa Sistemas S.A. de C.V.",
    "website": "https://www.odoo-community.org",
    "category": "Warehouse Management",
    "license": "AGPL-3",
    "depends": [
        "stock_analytic",
        "stock_project_analytic",
    ],
    "data": [
        "views/stock_move_views.xml",
        "views/stock_inventory_views.xml",
    ],
    'installable': True,
}
