from odoo import models, fields
from odoo.exceptions import UserError

class AssetAssignWizard(models.TransientModel):
    _name = 'asset.assign.wizard'
    _description = 'Wizard to assign assets to employee requests'

    request_id = fields.Many2one('employee.assets.request', readonly=True)
    employee_id = fields.Many2one(related='request_id.employee_id', readonly=True)
    asset_type = fields.Many2one(related='request_id.asset_type', readonly=True)
    quantity = fields.Integer(related='request_id.quantity', readonly=True)
    asset_ids = fields.Many2many(
        'account.asset',
        domain="[('asset_state','=','available'), ('model_id','=',asset_type)]"
    )

    def action_confirm_assign(self):
        if len(self.asset_ids) != self.quantity:
            raise UserError("Selected assets must match requested quantity.")

        self.asset_ids.write({'asset_state': 'assigned'})
        self.request_id.assigned_asset_ids = [(6, 0, self.asset_ids.ids)]
        self.request_id.assigned_asset_id = self.asset_ids[0].id if self.asset_ids else False
        self.request_id.state = 'assigned'
        self.request_id.assigned_date = fields.Datetime.now()