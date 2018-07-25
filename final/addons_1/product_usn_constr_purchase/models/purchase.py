from odoo import api, models, fields


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.onchange('product_qty')
    def product_qty_change(self):
        if self.product_qty != 1:
            if self.product_id.product_tmpl_id.tracking == 'serial':
                self.product_qty = 1
                raise models.ValidationError(
                    'You cannot order more than one item of this product. Try another line.')
