from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


DeclarativeBase = declarative_base()

def db_connect():
	"""
	Performs database connection using database settings from settings.py.
	Returns sqlalchemy engine instance
	"""
	return create_engine(URL(**settings.DATABASE))


def create_deals_table(engine):
	""""""
	DeclarativeBase.metadata.create_all(engine)


class Deals(DeclarativeBase):
	"""sqlalchemy deals model"""
	__tablename__ = "deals"

	id = Column(Integer, primary_key=True)
	title = Column('title', String)
	url = Column('url', String)
	