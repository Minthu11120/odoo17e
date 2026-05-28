from odoo import fields, models, api
from odoo.exceptions import UserError


class EmployeeAssetsRequest(models.Model):
    _name = 'employee.assets.request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Employee Assets Request'
    _order = 'name desc'

    name = fields.Char(default='New', copy=False, string='Request ID')
    employee_id = fields.Many2one('hr.employee', required=True, default=lambda self: self.env['hr.employee'].search(
        [('user_id', '=', self.env.uid), ('active', '=', True)],
        limit=1))
    department_id = fields.Many2one(related='employee_id.department_id')
    manager_id = fields.Many2one(related='employee_id.parent_id', required=True)
    asset_type = fields.Many2one('account.asset',
                                 string="Assets Type",
                                 required=True,
                                 tracking=True,
                                 domain="[('state','=','model')]")
    quantity = fields.Integer(default=1)
    reason = fields.Text()
    state = fields.Selection([
        ('draft', 'Draft'), ('submitted', 'Submitted'), ('manager_approved', 'Manager Approved'), ('assigned', 'Assigned'), ('rejected', 'Rejected'), ('cancelled', 'Cancelled')
    ], default='draft', tracking=True)
    assigned_asset_ids = fields.Many2many('account.asset', string='Assigned Assets IDs')
    request_date = fields.Datetime(default=fields.Datetime.now)
    assigned_date = fields.Datetime('Assigned Date')
    is_current_manager = fields.Boolean(
        compute='_compute_is_current_manager',
        store=False
    )
    assigned_asset_id = fields.Many2one('account.asset',string='Assigned Asset')

    @api.depends('manager_id')
    def _compute_is_current_manager(self):
        for rec in self:
            rec.is_current_manager = (
                    rec.manager_id
                    and rec.manager_id.user_id
                    and rec.manager_id.user_id.id == self.env.uid
            )


    @api.model_create_multi
    def create(self, vals_list):
        res = super(EmployeeAssetsRequest, self).create(vals_list)
        res.write({
            'name': self.env['ir.sequence'].sudo().next_by_code('employee.assets.request'),
        })
        return res

    def action_submit(self):
        self.ensure_one()

        if self.quantity <= 0:
            raise UserError("Quantity must be greater than zero before submitting.")

        self.state = 'submitted'

        # Send email notification
        template = self.env.ref(
            'employee_assets.email_asset_request_submitted',
            raise_if_not_found=False
        )
        if template:
            template.send_mail(self.id, force_send=True)

        if not self.manager_id or not self.manager_id.user_id:
            raise UserError("Manager user is not configured.")

        activity_type = self.env.ref(
            'employee_assets.mail_activity_asset_request_approval'
        )

        if self.manager_id.user_id:
            self.activity_schedule(
                activity_type_id=activity_type.id,
                user_id=self.manager_id.user_id.id,
                summary="Approve Asset Request",
                note=f"""
                    Please review asset request:
                    <br/><b>Employee:</b> {self.employee_id.name}
                    <br/><b>Asset Type:</b> {self.asset_type}
                    <br/><b>Quantity:</b> {self.quantity}
                    """
            )

    def action_manager_approve(self):
        self.state = 'manager_approved'


    def action_reject(self):
        self.state = 'rejected'

    def action_cancelled(self):
        self.state = 'cancelled'

    def reset_to_draft(self):
        self.state = 'draft'

    def action_open_assign_asset_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Assign Assets',
            'res_model': 'asset.assign.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_request_id': self.id}
        }

