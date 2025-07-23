from odoo import models, fields, _, api
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_round
from odoo.tools import format_date

class ExpenseSheetInheritance(models.Model):
    _inherit = 'hr.expense.sheet'

    state = fields.Selection(
        selection_add=[('head_approve', 'Head approve'),('hr_approve', 'Hr approve'),('accounts_approve',  'Accounts Approve')],
        ondelete={
            'head_approve': 'cascade',
            'hr_approve': 'cascade',
            'accounts_approve': 'cascade'
        },
    )

    def act_submit_to_head(self):
        self.state = 'head_approve'

    def act_submit_to_hr(self):
        self.state = 'hr_approve'

    def act_submit_to_accounts(self):
        self.state = 'approve'


class ExpenseInheritance(models.Model):
    _inherit = 'hr.expense'

    # def _get_default_expense_sheet_values(self):
    #     # Filter expenses that have a non-zero amount and valid quantity
    #     expenses_with_amount = self.filtered(lambda expense: not (
    #             expense.currency_id.is_zero(expense.total_amount_currency)
    #             or expense.company_currency_id.is_zero(expense.total_amount)
    #             or (expense.quantity and not float_round(expense.quantity,
    #                                                      precision_rounding=expense.product_uom_id.rounding))
    #     ))
    #
    #     if any(expense.state != 'draft' or expense.sheet_id for expense in expenses_with_amount):
    #         raise UserError(_("You cannot report twice the same line!"))
    #     if not expenses_with_amount:
    #         raise UserError(_("You cannot report the expenses without amount!"))
    #     if len(expenses_with_amount.mapped('employee_id')) != 1:
    #         raise UserError(_("You cannot report expenses for different employees in the same report."))
    #     if len(self.company_id) != 1:
    #         raise UserError(_("You cannot report expenses for different companies in the same report."))
    #
    #     # Check if two reports should be created (own_account vs company_account)
    #     own_expenses = expenses_with_amount.filtered(lambda x: x.payment_mode == 'own_account')
    #     company_expenses = expenses_with_amount - own_expenses
    #     create_two_reports = own_expenses and company_expenses
    #
    #     sheets = (own_expenses, company_expenses) if create_two_reports else (expenses_with_amount,)
    #     values = []
    #
    #     # Generate report values
    #     for todo in sheets:
    #         paid_by = 'company' if todo[0].payment_mode == 'company_account' else 'employee'
    #         sheet_name = _("New Expense Report, paid by %(paid_by)s", paid_by=paid_by) if len(sheets) > 1 else False
    #         if len(todo) == 1:
    #             sheet_name = todo.name
    #         else:
    #             dates = todo.mapped('date')
    #             if False not in dates:
    #                 min_date = format_date(self.env, min(dates))
    #                 max_date = format_date(self.env, max(dates))
    #                 if min_date == max_date:
    #                     sheet_name = min_date
    #                 else:
    #                     sheet_name = _("%(date_from)s - %(date_to)s", date_from=min_date, date_to=max_date)
    #
    #         values.append({
    #             'company_id': self.company_id.id,
    #             'employee_id': self[0].employee_id.id,
    #             'name': sheet_name,
    #             'expense_line_ids': [Command.set(todo.ids)],
    #             'state': 'draft',
    #         })
    #     return values

    # product_id = fields.Many2one(
    #     comodel_name='product.product',
    #     string="Category",
    #     tracking=True,
    #     check_company=True,
    #     domain=[('can_be_expensed', '=', True)],
    #     ondelete='restrict',
    #     required=False,
    # )

