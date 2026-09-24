from odoo import api, fields, models
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = "res.partner"

    cl = fields.Float(string="Credit Limit", default=1000.0)
