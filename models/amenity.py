#!/usr/bin/python3
""" State Module for HBNB project """
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

storage_type = environ.get('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    """ Stores the amenities for a place
    """
    if storage_type == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        __tablename__ = 'amenities_file'
        name = ""
