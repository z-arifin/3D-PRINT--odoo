# -*- coding: utf-8 -*-
{
    'name': "3D PRINT",

    'summary': """
        3D PRINTING SYSTEM MANAGEMENT""",

    'description': """
        Sistem manajemen dari percetakan 3D
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/3dprint_views.xml',
        'views/3dprint_caracetak.xml',
        'views/3dprint_ordercetak.xml',
        'views/3dprint_contact.xml',
        'views/3dprint_contact_pegawai.xml',
        'views/templates.xml',
        'report/report.xml',
        'report/orderinvoice.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}