from odoo import fields, models

class AccountAsset(models.Model):
    _inherit = 'account.asset'

    asset_serial_no = fields.Char()
    asset_state = fields.Selection([
        ('available', 'Available'),
        ('assigned', 'Assigned'),
    ], default='available')