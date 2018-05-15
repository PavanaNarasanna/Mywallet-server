from graphene_sqlalchemy import SQLAlchemyObjectType
from server.models import (Expense as ExpenseModel)


class Expense(SQLAlchemyObjectType):
    class Meta:
        model = ExpenseModel

def resolve_expense(info, user_id= None):
    query = Expense.get_query(info)
    if user_id:
        query = query.filter(ExpenseModel.user_id == user_id)
    else:
        query = query.filter(ExpenseModel.user_id == None)
    return query.all()
