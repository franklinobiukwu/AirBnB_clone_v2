#!/usr/bin/python3
""" State Module for HBNB project """
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City

storage_type = environ.get('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    if storage_type == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="delete",
                              backref="state")
    else:
        __tablename__ = 'states_file'
        name = ""

        @property
        def cities(self):
            """ Obtains the cities for a state """
            from models import storage

            my_cities = []
            my_dict = storage.all(City)

            for key, value in my_dict.items():
                if (value.state_id == self.id):
                    my_cities.append(value)

            return (my_cities)
