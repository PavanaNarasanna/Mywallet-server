from sqlalchemy import (Column, ForeignKey, String, Integer, DateTime, Boolean, Enum, Text, Float, func)
from sqlalchemy.orm import (backref, relationship)
from sqlalchemy_utils import force_auto_coercion
from server.database import Base
from .category import Category
force_auto_coercion()

class Sub_Category(Base):
    __tablename__ = 'sub_category'

    id = Column(Integer, primary_key=True)
    category_id = Column(
        Integer,
        ForeignKey(
            'categorys.id',
            name="CATEGORY"),
        nullable=True)
    category=relationship(
        Category,
        foreign_keys='Sub_Category.category_id',
        backref=backref(
            'sub_category',
            uselist=True,
            cascade='delete,all'
        ))
    sub_category_name = Column(Text, nullable=True)