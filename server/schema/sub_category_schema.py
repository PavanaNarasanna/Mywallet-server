from graphene_sqlalchemy import SQLAlchemyObjectType
from server.models import (Sub_Category as Sub_CategoryModel)
from server.database import db_session

class Sub_Category(SQLAlchemyObjectType):
    class Meta:
        model = Sub_CategoryModel

def resolve_sub_category(info, category_id = None, user_id = None):
    query = Sub_Category.get_query(info)
    if category_id and user_id:
        query = query.filter(Sub_CategoryModel.category_id == category_id , Sub_CategoryModel.user_id == user_id)
    else:
        query = query.filter(Sub_CategoryModel.user_id == None)
    return query.all()

def update_sub_category(info, id=None, category_id=None, sub_category_name=None, user_id=None):
    query = Sub_Category.get_query(info)
    if id:
        to_update = {"category_id": category_id, "sub_category_name": sub_category_name, "user_id": user_id}
        query.\
            filter(Sub_CategoryModel.id == id).\
            update({k: v for k, v in to_update.items() if v is not None})
        db_session.commit()
    query = query.filter(Sub_CategoryModel.id == id)
    return query.first()
