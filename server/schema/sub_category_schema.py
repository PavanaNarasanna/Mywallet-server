from graphene_sqlalchemy import SQLAlchemyObjectType
from server.models import (Sub_Category as Sub_CategoryModel)


class Sub_Category(SQLAlchemyObjectType):
    class Meta:
        model = Sub_CategoryModel

def resolve_sub_category(info):
    return Sub_Category.get_query(info).all()

