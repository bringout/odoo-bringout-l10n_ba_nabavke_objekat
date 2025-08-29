from odoo import api, fields, models
from datetime import datetime

class PurchaseOrderLine(models.Model):
    """ class for inherited model purchase order line. Contains a field for line
        numbers and a function for computing line numbers.
    """

    _inherit = 'purchase.order.line'

    date_planned_date = fields.Date(string='Date planned - date only', compute='_compute_date_planned_date', store=False)

    
    @api.depends('date_planned')
    def _compute_date_planned_date(self):
        for line in self:
            line.date_planned_date = line.date_planned.date()


