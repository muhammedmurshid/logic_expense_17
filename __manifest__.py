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
        'base', 'hr', 'hr_expense'
    ],
    'data': [
        'security/groups.xml',
        'security/rules.xml',
        'views/expense.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,

}
