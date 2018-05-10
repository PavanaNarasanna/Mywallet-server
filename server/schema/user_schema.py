from graphene_sqlalchemy import SQLAlchemyObjectType
from server.models import (User as UserModel)


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel

def resolve_user(info):
    return User.get_query(info).all()