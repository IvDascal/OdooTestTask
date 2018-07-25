{
    'name': 'Sales orders documents',
    'description': """
This module add documents button to sale orders form.
    """,
    'depends': [
        'sale',
        'document'
    ],
    'data': [
        'views/sale_views.xml'
    ],
    'installable': True,
}
