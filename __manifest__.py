# -*- coding: utf-8 -*-
{
    'name': "citasmja",
    'summary': """Administrar citas.""",
    'description': """Descripción del módulo para citas de la tarea 04 de SGE""",
    'author': "Miguel Francisco Jurado Armesto",
    'website': "http://www.citasmja.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
	'auto_install': False,

}