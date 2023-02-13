# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    temp_quantity = fields.Float(string='Quantité', required=True, default=1.0)
    days_count = fields.Float(string="Nombre de Jours", default=1.0)

    @api.onchange('temp_quantity', 'days_count')
    def change_original_quantity(self):
    	for record in self:
    		if record.temp_quantity > 0 and record.days_count > 0:
    			record.product_uom_qty = record.temp_quantity * record.days_count
    		else:
    			record.product_uom_qty = 0

    def _prepare_invoice_line(self):
        self.ensure_one()
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res['days_count'] = self.days_count
        res['temp_quantity'] = self.temp_quantity
        return res

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    temp_quantity = fields.Float(string='Quantité', required=True, default=1.0, store=True)
    days_count = fields.Float(string="Nombre de jours", default=1.0, store=True)

    @api.onchange('temp_quantity', 'days_count')
    def change_original_quantity(self):
    	for record in self:
    		if record.temp_quantity > 0 and record.days_count > 0:
    			record.quantity = record.temp_quantity * record.days_count
    		else:
    			record.quantity = 0
