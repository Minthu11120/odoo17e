{
    'name': 'Employee Assets Management',
    'version': '17.0.1.0.1',
    'category': 'Employee',
    'summary': """Employee Assets Request Management is to manage the employee assets.""",
    'description': """Employee Assets Request Management module, manager can 
    enhance efficiency, control assets.""",
    'author': 'Pyae Sone Kyaw',
    'company': 'Blue Stone Solutions',
    'maintainer': 'Blue Stone Solutions',
    'depends': ['hr','mail','account_asset'],
    'assets': {
    },
    'data': [
        'views/account_asset_view.xml',
        'security/employee_assets_request_groups.xml',
        'views/employee_asset_views.xml',
        'views/employee_assets_request_menu.xml',
        'wizard/asset_assign_wizard_views.xml',
        'data/sequence.xml',
        'data/mail_template.xml',
        'data/mail_activity_type.xml',
        'security/ir.model.access.csv',

    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
