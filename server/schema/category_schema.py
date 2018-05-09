from graphene_sqlalchemy import SQLAlchemyObjectType
from server.models import (Category as CategoryModel)


class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel

def resolve_category(info):
    return Category.get_query(info).all()