#!/usr/bin/python3
""" State Module for HBNB project """
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

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
