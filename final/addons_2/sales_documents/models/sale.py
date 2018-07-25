from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit =["sale.order"]

    sale_order_documents_count = fields.Integer(compute='_compute_sale_order_documents_count', string='Documents')
    
    @api.multi
    def sale_order_doc(self):
        print('CALL sale_order_doc')

    def _compute_sale_order_documents_count(self):
        
        return 42
