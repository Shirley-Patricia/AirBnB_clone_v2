#!/usr/bin/python3
from os import environ
from sqlalchemy import create_engine
from models.base_model import Base
USR = environ['HBNB_MYSQL_USER'] = 'hbnb_dev'
PWD = environ['HBNB_MYSQL_PWD'] = 'hbnb_dev_pwd'
HST = environ['HBNB_MYSQL_HOST'] = 'localhost'
DB = environ['HBNB_MYSQL_DB'] = 'hbnb_dev_db'

class DBStorage():
	__engine = None
	__session = None
	def __init__(self):
		self.__engine = create_engine('mysql+mysqldb://USR:PWD@HST/DB', pool_pre_ping=True)
		Base.metadata.create_all(self.engine)
