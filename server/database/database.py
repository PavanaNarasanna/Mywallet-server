from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (scoped_session, sessionmaker)
from sqlalchemy_searchable import make_searchable
from sqlalchemy.orm import configure_mappers

from server.config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, convert_unicode=True)
configure_mappers()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
