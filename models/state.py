#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from models import storage
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', backref='state', passive_deletes=True, cascade="all, delete")

    @property
    def cities(self):
        """ returns the list of City instances with state_id
            equals to the current State.id
        """
        list_cities = storage.all(City)
        cities = []
        for value in list_cities.values():
            if value.state_id == self.id:
                cities.append(value)
        return cities
