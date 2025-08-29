from odoo import api, fields, models

class PurchaseOrder(models.Model):
 
    _inherit = 'stock.picking'
    
    origin_objekat_name = fields.Char(string='Objekat', compute='_compute_objekat', help='Naziv objekta', store=False)

    @api.depends('origin')
    def _compute_objekat(self):

        for rec in self:
            haveOrigin = False
            if rec.origin:
                haveOrigin = True
                po = self.env['purchase.order'].search(
                    [
                        ( 'name', '=', rec.origin),
                        ( 'company_id', '=', self.env.company.id),
                    ], limit=1)

            if haveOrigin:
                rec.origin_objekat_name = po.objekat_name
            else:
                rec.origin_objekat_name = '-'