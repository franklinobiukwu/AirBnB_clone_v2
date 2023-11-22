#!/usr/bin/python3
""" Place Module for HBNB project """
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


storage_type = environ.get('HBNB_TYPE_STORAGE')


place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60),
           ForeignKey('places.id'),
           primary_key=True,
           nullable=False),
    Column('amenity_id',
           String(60),
           ForeignKey('amenities.id'),
           primary_key=True,
           nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    if storage_type == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True, default='')
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True, default=0)
        longitude = Column(Float, nullable=True, default=0)
        reviews = relationship('Review', cascade='delete', backref='place')
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False,
                                 backref="place_amenities")
    else:
        __tablename__ = 'places_file'
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """
            Returns a list of reviews for the current
            place instance
            """
            from models import storage
            list_of_reviews = []
            objs = {}

            objs = storage.all("Review")

            for value in objs.values():
                if (value.place_id == self.id):
                    list_of_reviews.append(value)

            return (list_of_reviews)
