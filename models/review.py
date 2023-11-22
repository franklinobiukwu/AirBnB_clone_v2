#!/usr/bin/python3
""" Review module for the HBNB project """
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


storage_type = environ.get('HBNB_TYPE_STORAGE')


class Review(BaseModel, Base):
    """ Review classto store review information """
    if storage_type == 'db':
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        __tablename__ = 'reviews_file'
        place_id = ""
        user_id = ""
        text = ""
