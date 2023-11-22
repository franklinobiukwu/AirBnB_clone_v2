#!/usr/bin/python3
""" City Module for HBNB project """
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

storage_type = environ.get('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if storage_type == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', cascade='delete', backref='cities')
    else:
        __tablename__ = 'cities_file'
        state_id = ""
        name = ""
