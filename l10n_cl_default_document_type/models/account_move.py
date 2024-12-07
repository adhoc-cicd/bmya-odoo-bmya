from odoo import models


class AccountMove(models.Model):
    _inherit = 'account.move'


    def _compute_l10n_latam_document_type(self):
        for r in self:
            doc_types = r.l10n_latam_available_document_type_ids._origin
            invoice_type = r.move_type
            doc_types_dict = {
                doc_type.code: doc_type for doc_type in self.l10n_latam_available_document_type_ids._origin}
            taxpayer_type = r.partner_id.l10n_cl_sii_taxpayer_type
            if taxpayer_type in ['1', '2']:
                code = 72 if invoice_type == 'in_invoice' else 33
                r.l10n_latam_document_type_id = doc_types_dict.get(code, False)
            elif taxpayer_type == '3':
                r.l10n_latam_document_type_id = doc_types_dict.get('39', False)
            else:  # taxpayer_type == '4'
                r.l10n_latam_document_type_id = doc_types_dict.get('110', False)
        # super(AccountMove, self - taxpayer_moves)._compute_l10n_latam_document_type()
