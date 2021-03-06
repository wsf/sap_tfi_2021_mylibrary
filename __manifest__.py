# -*- coding: utf-8 -*-
{
    'name': "My Library999",  # Module title
    'summary': "Manage books easily999",  # Module subtitle phrase
    'description': """
Manage Library
==============
Description related to library.
    """,  # Supports reStructuredText(RST) format
    'author': "Parth Gajjar999",
    'website': "http://www.example.com",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/library_book_categ.xml',
        'views/library_book_rent.xml',
        'wizard/library_book_rent_wizard.xml',
        'wizard/library_book_return_wizard.xml',
        'views/library_book_statistics.xml',
        'views/res_config_settings_views.xml'
    ],
    'post_init_hook': 'add_book_hook',
    # This demo data files will be loaded if db initialize with demo data (commented because file is not used in this example)
    # 'demo': [
    #     'data/demo.xml'
    # ],

    'installable': True,
    'application': True,
    'auto_install': False,

}
