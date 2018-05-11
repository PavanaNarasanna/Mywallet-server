from .database import db_session
from server.models.expense import (Expense as ExpenseModel)


class Expenses:
    def insert_expense(self, expense):
        expense = ExpenseModel(
            sub_category_id=expense.sub_category_id,
            item=expense.item,
            unit=expense.unit,
            quantity=expense.quantity,
            provider=expense.provider,
            price=expense.price,
            category_id=expense.category_id,
            user_id=expense.user_id
        )

        db_session.add(expense)
        db_session.commit()
        return expense
