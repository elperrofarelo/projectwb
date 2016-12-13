# -*- coding: utf-8 -*-
# <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class PurchaseRequestLineMakePurchaseOrderItem(models.TransientModel):
    _name = "purchase.request.line.make.purchase.order.item"
    _inherit = "purchase.request.line.make.purchase.order.item"

    product_qty = fields.Float(string='Quantity to purchase',
                               digits=(14, 5),)
    is_project_insume = fields.Boolean()
    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product',
        )
    product_uom_id = fields.Many2one(
        comodel_name='product.uom',
        string='UoM',)


class PurchaseRequestLineMakePurchaseOrder(models.TransientModel):
    _inherit = "purchase.request.line.make.purchase.order"

    @api.model
    def _prepare_item(self, line):
        res = super(
            PurchaseRequestLineMakePurchaseOrder, self)._prepare_item(line)
        res['is_project_insume'] = True
        return res

    @api.model
    def _prepare_purchase_order_line(self, po, item):
        res = (
            super(PurchaseRequestLineMakePurchaseOrder, self).
            _prepare_purchase_order_line(po, item))
        res['is_project_insume'] = item.is_project_insume
        return res