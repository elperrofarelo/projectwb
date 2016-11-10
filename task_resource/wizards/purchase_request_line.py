# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from openerp import fields, models


class PurchaseRequestLine(models.TransientModel):

    _name = 'purchase.request.line.wizard'
    _description = 'Wizard of purchase request'

    wiz_id = fields.Many2one('purchase.request.wizard')
    line_id = fields.Many2one(
        'analytic.resource.plan.line',
        string='Resource Line',
        required=True,
        readonly=True)
    analytic_account_id = fields.Many2one(
        'account.analytic.account',
        related='line_id.account_id',
        string='Analytic Account',
        readonly=True)
    product_id = fields.Many2one(
        'product.product',
        string='Product',
        readonly=True)
    description = fields.Char(
        string='Description',
        required=True)
    uom_id = fields.Many2one('product.uom', string='UoM')
    qty = fields.Float(
        string='Quantity Planned',
        readonly=True)
    qty_on_hand = fields.Float(
        string='Quantity On Hand',
        readonly=True)
    qty_to_request = fields.Float(
        string="Quantity To Request",
        default="1.0")