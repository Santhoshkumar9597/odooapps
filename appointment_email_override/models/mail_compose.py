from odoo import models

class MailComposeMessage(models.TransientModel):
    _inherit = 'mail.compose.message'

    def _action_send_mail(self, *args, **kwargs):

        for wizard in self:
            if wizard.model == 'calendar.event':

                template = wizard.template_id

                if template and template.email_from:
                    wizard.email_from = template.email_from

        return super()._action_send_mail(*args, **kwargs)