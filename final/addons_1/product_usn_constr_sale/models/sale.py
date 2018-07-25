from odoo import api, models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_uom_qty')
    def product_uom_qty_change(self):
        if self.product_uom_qty != 1:
            if self.product_id.product_tmpl_id.tracking == 'serial':
                self.product_uom_qty = 1
                
                raise models.ValidationError(
                    'You cannot order more than one item of this product. Try another line.')
