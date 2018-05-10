from sqlalchemy import (Column, ForeignKey, String, Integer, DateTime, Boolean, Enum, Text, Float, func)
from sqlalchemy_utils import force_auto_coercion
from sqlalchemy.orm import (backref, relationship)
from server.database import Base
from .category import Category
from .sub_category import Sub_Category
from .user import User
force_auto_coercion()


class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    sub_category_id = Column(
        Integer,
        ForeignKey(
            'sub_category.id',
            name="SUBCATEGORY"),
        nullable=True)
    SUBCATEGORY=relationship(
        Sub_Category,
        foreign_keys='Expense.sub_category_id',
        backref=backref(
            'expenses',
            uselist=True,
            cascade='delete,all'
        )
    )
    item= Column(Text, nullable=True)
    unit= Column(Text, nullable=True)
    quantity= Column(Integer, nullable=True)
    provider= Column(Text, nullable=True)
    price= Column(Float, nullable=True)
    user_id = Column(
        Integer,
        ForeignKey(
            'users.id',
            name="USER"),
            nullable=True)
    USER=relationship(
        User,
        foreign_keys='Expense.user_id',
        backref=backref(
            'expenses',
            uselist=True,
            cascade='delete,all'
        )
    )
    created_at = Column(DateTime, default=func.now(), nullable=True)
