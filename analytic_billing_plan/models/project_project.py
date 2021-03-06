# -*- coding: utf-8 -*-
# Copyright <2016> <Jarsa Sistemas, S.A. de C.V.>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class ProjectProject(models.Model):
    _inherit = 'project.project'

    billing_project_total = fields.Float(
        'Billing Total',
        compute='_compute_billing_project_total',)

    @api.multi
    def _compute_billing_project_total(self):
        for rec in self:
            wbs_elements = self.env['project.wbs_element'].search([
                ('project_id', '=', rec.id)])
            if wbs_elements:
                for wbs_element in wbs_elements:
                    rec.billing_project_total += (
                        wbs_element.billing_concept_total)
            else:
                rec.billing_project_total = 0.0
