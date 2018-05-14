from graphene_sqlalchemy import SQLAlchemyObjectType
from server.models import (Category as CategoryModel)


class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel

def resolve_category(info, user_id= None):
    query = Category.get_query(info)
    if id:
        query = query.filter(CategoryModel.user_id == user_id)
    return query.all()