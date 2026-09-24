from odoo import api, fields, models
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = "res.partner"

    credit_limit = fields.Float(string="Credit Limit", default=1000.0)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    is_over_credit = fields.Boolean(
        string="Over Credit Limit",
        compute="_compute_is_over_credit",
        store=True,
    )

    @api.depends("partner_id", "amount_total")
    def _compute_is_over_credit(self):
        """If total uninvoiced/draft sales for this customer exceed their credit limit,
        flag the order as over credit.
        """
        for o in self:
            tp = sum(self.env["sale.order"].search([
                ("partner_id", "=", o.partner_id.id),
                ("state", "in", ["draft", "sent"])
            ]).mapped("amount_total"))
            # if more than partner level set to true
            if tp >= 5000:
                o.is_over_credit = 1
            else:
                o.is_over_credit = 0

    def action_confirm(self):
        for o in self:
            if o.is_over_credit:
                o.sudo().write({"state": "draft"})
                raise UserError("Order cannot be confirmed: Customer is over credit limit!")

        return True
