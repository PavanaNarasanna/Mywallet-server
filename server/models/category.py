from sqlalchemy import (Column, String, Integer)
from sqlalchemy_utils import force_auto_coercion
from server.database import Base

force_auto_coercion()


class Category(Base):
    __tablename__ = 'categorys'
    id = Column(Integer, primary_key=True)
    category_name = Column(String(45), nullable=True)
   