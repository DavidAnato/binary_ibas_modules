from odoo import models, fields


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def _get_record_and_check(self, xmlid=None, model=None, id=None, field='datas', access_token=None):
        # Override using super if user is allowed
        if self.sudo().env.user.allow_preview:
            return super(IrHttp, self.sudo())._get_record_and_check(xmlid, model, id, field, access_token)
        else:
            return super(IrHttp, self)._get_record_and_check(xmlid, model, id, field, access_token)


class Users(models.Model):
    _inherit = 'res.users'

    allow_preview = fields.Boolean(
        string='Allow Preview',
        default=True,
        help='It allows the user to preview all attachments (Use at your own risk)',
    )
