from odoo import fields, models, api


class L10nLatamDocumentType(models.Model):
    _inherit = 'l10n_latam.document.type'

    fiscal_position_id = fields.Many2one('account.fiscal.position', string='Fiscal Position')
