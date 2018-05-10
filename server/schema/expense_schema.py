from graphene_sqlalchemy import SQLAlchemyObjectType
from server.models import (Expense as ExpenseModel)


class Expense(SQLAlchemyObjectType):
    class Meta:
        model = ExpenseModel

def resolve_expense(info):
    return Expense.get_query(info).all()
