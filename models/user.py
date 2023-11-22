#!/usr/bin/python3
"""This module defines a class User"""
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

storage_type = environ.get('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    if storage_type == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True, default='')
        last_name = Column(String(128), nullable=True, default='')
        places = relationship("Place", cascade="delete", backref="user")
        reviews = relationship('Review', cascade='delete', backref='user')
    else:
        __tablename__ = 'users_file'
        email = ''
        password = ''
        first_name = ''
        last_name = ''
