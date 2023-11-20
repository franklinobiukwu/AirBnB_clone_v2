#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from os import environ
from sqlalchemy import Column, String, ForeignKey
from models.city import City
from sqlalchemy.orm import relationship

Base = declarative_base()

class State(BaseModel, Base):
    """ State class """

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'

        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="delete", backref="state")
    else:
        name = ''
        cities = []

    if environ.get('HBNB_TYPE_STORAGE') == 'fs':
        @property
        def cities(self):
            """Getter attribute for cities in file storage"""
            from models import storage
            city_list = []
            for city in storage.all('City').values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
