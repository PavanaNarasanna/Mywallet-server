from sqlalchemy import (Column, ForeignKey, String, Integer, DateTime, Boolean, Enum, Text, Float, func)
from sqlalchemy_utils import force_auto_coercion
from sqlalchemy.orm import (backref, relationship)
from server.database import Base
force_auto_coercion()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    user_name = Column(String, nullable=True)
    password = Column(String, nullable=True)
    role = Column(String, nullable=True)
    email_id= Column(String, nullable=True)
    last_login = Column(DateTime,nullable=True)
    created_date = Column(DateTime, default=func.now(), nullable=True)
    updated_date = Column(DateTime, default=func.now(), nullable=True)
    created_by_id = Column(Integer,nullable=True)
    updated_by_id = Column(Integer, nullable=True)
   