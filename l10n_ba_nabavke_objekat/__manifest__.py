{
    'name': 'Nabavke broj objekta',
    'version': '16.0.2.0.0',
    'category': 'Extra Tools',
    'summary': 'Broj objekta na narudžbenici dobavljača.',
    'author': 'bring.out doo Sarajevo',
    'website': "https://www.bring.out.ba",
    'license': 'AGPL-3',
    'depends': ['base', 'purchase', 'purchase_analytic', 'l10n_ba_sifra_in_documents'],
    'data': [
        'views/report_purchaseorder_document_view.xml',
        'views/stock_picking_list.xml',
        
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
