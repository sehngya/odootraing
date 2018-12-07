# -*- coding: utf-8 -*-
{
    'name': 'pscloud培训作业',

    'summary': '',

    'description': '培训测试',

    'author': '王圣亚',
    'website': 'https://www.mypscloud.com/'',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/res_partner_views.xml',
        'views/training_subject_views.xml',
        'views/training_views.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}