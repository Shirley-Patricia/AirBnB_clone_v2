#!/usr/bin/python3
''' ghjklerthedh '''
import os
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


USR = os.getenv('HBNB_MYSQL_USER')
PWD = os.getenv('HBNB_MYSQL_PWD')
HST = os.getenv('HBNB_MYSQL_HOST')
DB = os.getenv('HBNB_MYSQL_DB')


class DBStorage():
    ''' asdfghj '''
    __engine = None
    __session = None

    def __init__(self):
        ''' regyhfsd '''
        self.__engine = create_engine(
            'mysql+mysqldb://USR:PWD@HST/DB', pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """ This method returns all objects depending of the class name """
        dictio = {}

        if cls:
            for item in self.__session.query(cls).all():
                dictio[item.__class__.__name__ + '.' + item.id] = item
        else:
            for clase_in in self.clases_objects:
                for item in self.__session.query(clase_in).all():
                    dictio[item.__class__.__name__ + '.' + item.id] = item

        return dictio

    def new(self, obj):
        ''' rhgjgfd '''
        self.__session.add(obj)

    def save(self):
        ''' ghjhgf '''
        self.__session.commit()

    def reload(self):
        """ This method creates all tables in the database
            and creates the current database session """
        Base.metadata.create_all(self.__engine)
        session2 = sessionmaker(bind=self.__engine,
                                expire_on_commit=False)
        Session = scoped_session(session2)
        self.__session = Session()
