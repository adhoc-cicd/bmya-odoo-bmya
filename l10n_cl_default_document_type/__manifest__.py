{
    "name": "Default Document Type (Chilean Localization)",
    'summary': 'Automatically set a document type depending on the customer\'s taxpayer type.',
    "description": """
        Depending on the partner's taxpayer type we set the default document type to the following:
        1st or 2nd category: Factura Electrónica (33) for sales.
        2nd category: Boleta de Honorarios (72) for purchases.
        End Consumer: Boleta Electrónica (39)
        Foreigner: Factura de Exportación (110)
        This module is recommended for Community edition, but it also improves feature for Enterprise edition, 
        since EE does not select Boleta de honorarios for taxpayer type 2.
    """,
    'version': '18.0.1.0.0',
    'category': 'Localization',
    'author': 'Blanco Martín & Asociados',
    'website': 'https://www.bmya.cl',
    'license': 'LGPL-3',
    'depends': ['l10n_cl'],
    'installable': True,
}
