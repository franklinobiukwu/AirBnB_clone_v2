#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import environ

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

storage_type = environ.get('HBNB_TYPE_STORAGE')

class State(BaseModel, Base):
    """ State class """
    if storage_type == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        __tablename__ = ''
        name = ""

        @property
        def cities(self):
            """Getter attribute for FileStorage"""
            from models import storage
            city_instances = storage.all('City')
            return [city for city in city_instances.values() if city.state_id == self.id]
