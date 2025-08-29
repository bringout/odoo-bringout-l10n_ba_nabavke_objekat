from odoo import api, fields, models

class PurchaseOrder(models.Model):
 
    _inherit = 'purchase.order'

    objekat_broj = fields.Char(string='Objekat broj', compute='_compute_objekat', help='Broj objekta', store=False)
    objekat_name = fields.Char(string='Objekat ime', compute='_compute_objekat', help='Ime objekta', store=False)
    
    @api.depends('product_id')
    def _compute_objekat(self):

        for rec in self:
            analytic = False
            if rec.analytic_distribution:
                for key in rec.analytic_distribution:
                    #print(int(key))
                    analytic = self.env['account.analytic.account'].search(
                    [
                        ( 'id', '=', int(key)),
                        ('company_id', '=', self.env.company.id),
                    ], limit=1)

            if analytic:
                rec.objekat_broj = analytic.code
                rec.objekat_name = analytic.name
            else:
                rec.objekat_broj = '0'
                rec.objekat_name = '-'
