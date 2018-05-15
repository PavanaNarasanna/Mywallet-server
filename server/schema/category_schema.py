from graphene_sqlalchemy import SQLAlchemyObjectType
from server.models import (Category as CategoryModel)


class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel

def resolve_category(info, user_id= None):
    query = Category.get_query(info)
    if user_id:
        query = query.filter(CategoryModel.user_id == user_id)
    else:
        query = query.filter(CategoryModel.user_id == None)
    return query.all()