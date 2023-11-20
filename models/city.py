#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from os import environ

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"

    if (environ.get("HBNB_TYPE_STORAGE", "file") == "db"):
        name = Column(String(128), nullable=False)
        state_id = Column(ForeignKey("states.id"),
                          nullable=False)
        places = relationship("Place", cascade="delete",
                              backref="cities")
    else:
        name = ""
        state_id = ""
