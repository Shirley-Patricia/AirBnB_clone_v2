#!/usr/bin/python3
'''
    creating a new engine
    and link it with the db
'''
import os
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.schema import MetaData
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


USR = os.getenv('HBNB_MYSQL_USER')
PWD = os.getenv('HBNB_MYSQL_PWD')
HST = os.getenv('HBNB_MYSQL_HOST')
DB = os.getenv('HBNB_MYSQL_DB')
ENV = os.getenv('HBNB_ENV')


class DBStorage():
    ''' making the methods and sessions '''
    __engine = None
    __session = None

    def __init__(self):
        ''' initializate the engine '''
        self.__engine = create_engine(
            'mysql+mysqldb://USR:PWD@HST/DB', pool_pre_ping=True)
        if ENV == 'test':
            metadata = MetaData(self.__engine)
            metadata.reflect()
            metadata.drop_all()

    def all(self, cls=None):
        """ This method returns all objects depending of the class name """
        dictio = {}
        classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        if cls is not None:
            data = self.__session.query(classes[cls]).all()
            for dbs in data:
                dictio[dbs.__class__.__name__ + '.' + dbs.id] = dbs
        else:
            for clase_in in classes:
                data = self.__session.query(classes[clase_in]).all()
                for dbs in data:
                    dictio[dbs.__class__.__name__ + '.' + dbs.id] = dbs

        return dictio

    def new(self, obj):
        ''' add the obj to the current DB '''
        self.__session.add(obj)

    def save(self):
        '''
            commit all changes of the
            current database session
        '''
        self.__session.commit()

    def reload(self):
        """ This method creates all tables in the database
            and creates the current database session """
        Base.metadata.create_all(self.__engine)
        Session2 = sessionmaker(bind=self.__engine,
                                expire_on_commit=False)
        Session = scoped_session(Session2)
        self.__session = Session()

    def delete(self, obj=None):
        '''
            delete from the current database
            session obj if not None
        '''
        if obj is not None:
            self.__session.delete(obj)
