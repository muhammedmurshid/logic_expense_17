{
    'name': 'Logic Expense',
    'version': '1.0.0',
    'summary': 'logic Expenses',
    'description': """
        A more detailed description of the module.
    """,
    'author': 'Murshid',
    'website': 'https://www.yourwebsite.com',
    'category': 'Specific Category',
    'license': 'LGPL-3',
    'depends': [
        'base', 'mail', 'logic_payments_17', 'account', 'openeducat_core'
    ],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/user_rules.xml',
        'views/cancallation_wizard.xml',
        'views/expense_form_view.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,

}
