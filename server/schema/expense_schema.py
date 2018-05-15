from graphene_sqlalchemy import SQLAlchemyObjectType
from server.models import (Expense as ExpenseModel)
from server.database import db_session

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

def update_expense(info, id=None, sub_category_id=None, item=None, unit=None,quantity=None, provider=None, price=None, category_id=None, user_id=None):
    query = Expense.get_query(info)
    if id:
        to_update = {"sub_category_id": sub_category_id, "item": item, "unit": unit, "quantity": quantity, "provider": provider, "price": price, "category_id": category_id, "user_id": user_id}
        query.\
            filter(ExpenseModel.id == id).\
            update({k: v for k, v in to_update.items() if v is not None})
        db_session.commit()
    query = query.filter(ExpenseModel.id == id)
    return query.first()
