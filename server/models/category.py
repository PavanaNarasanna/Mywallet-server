from sqlalchemy import (Column, ForeignKey, String, Integer, DateTime, Boolean, Enum, Text, Float, func)
from sqlalchemy.orm import (backref, relationship)
from sqlalchemy_utils import force_auto_coercion
from server.database import Base
from .user import User
force_auto_coercion()


class Category(Base):
    __tablename__ = 'categorys'
    id = Column(Integer, primary_key=True)
    category_name = Column(String(45), nullable=True)
    user_id = Column(
        Integer,
        ForeignKey(
            'users.id',
            name="USER"),
            nullable=True)
    USER=relationship(
        User,
        foreign_keys='Category.user_id',
        backref=backref(
            'categorys',
            uselist=True,
            cascade='delete,all'
        )
    )
   
    created_at = Column(DateTime, default=func.now(), nullable=True)