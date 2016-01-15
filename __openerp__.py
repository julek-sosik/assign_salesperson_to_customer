# -*- coding: utf-8 -*-
{
    'name': "Assign Salesperson to many Customers at once.",

    'summary': """
        This module allows you to assign Salesperson to many companies at once.
    """,

    'description': """
        This module allows you to assign Salesperson to many companies at once.
    """,

    'author': "juliusz.sosinowicz@atteli.com",
    'website': "http://www.atteli.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['crm'],

    # always loaded
    'data': [
        'views/assign_salesperson_to_customer.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}