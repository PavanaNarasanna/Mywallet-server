from graphene_sqlalchemy import SQLAlchemyObjectType
from server.models import (Sub_Category as Sub_CategoryModel)


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

