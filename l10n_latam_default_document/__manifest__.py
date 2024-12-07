{
    'name': 'Default Latam Document',
    'version': '18.0.1.0.0',
    'summary': 'Default Latam Document',
    'description': """
        This module choose default Latam Document with the following criteria: it uses the sequence to
        order the documents, in an ascending order. So you can change the documents order to ensure the first in 
        sequence to be selected by default. This is recommended only for Odoo Community Edition.
    """,
    'category': 'Localization',
    'author': 'Blanco Martín & Asociados',
    'website': 'https://www.bmya.cl',
    'license': 'LGPL-3',
    'depends': ['l10n_latam_invoice_document'],
    'data': [
        'views/l10n_latam_document_type_view.xml',
    ],
    'installable': True,
    'auto_install': False
}
