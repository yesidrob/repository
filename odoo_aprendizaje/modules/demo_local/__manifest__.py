# -*- coding: utf-8 -*-
{
    'name': "demo local graficas",

    'summary': "muestra una grafica con los datos ingresados",

    'description': """
este modulo es un ejemplo de como crear una grafica en odoo con los datos ingresados por el usuario.
    """,

    'author': "Yesid",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/views.xml',
    ],
    'assets': {
        ['web.assets_backend',
        'demo_local/static/src/js/grafica.js',],
},
}

