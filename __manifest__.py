{
    'name': 'Partner Credit Limit',
    'version': '19.0.1.0.0',
    'summary': 'Add credit limit to partners and enforce it on sale order confirmation',
    'category': 'Sales',
    'depends': ['sale'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
