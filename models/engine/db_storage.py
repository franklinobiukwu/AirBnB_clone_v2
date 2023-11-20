#!/usr/bin/python3
"""
This module defines a class to manage
database storage for hbnb clone
"""
from os import environ
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """
    This class manages database operations
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Initializes the engine """
        user = environ.get("HBNB_MYSQL_USER")
        pwd = environ.get("HBNB_MYSQL_PWD")
        host = environ.get("HBNB_MYSQL_HOST", "localhost")
        db = environ.get("HBNB_MYSQL_DB")
        should_delete = environ.get("HBNB_ENV")

        url = f"mysql://{user}:{pwd}@{host}/{db}"
        self.__engine = create_engine(url, pool_pre_ping=True)

        if (should_delete == "tests"):
            Base.metadata.drop_all(__engine)
            return

    def all(self, cls=None):
        """
        Retrieves objects from the database.

        Parameters

            cls : class, optional
            The class of objects to retrieve.
            By default, all objects are fetched

        Return
            Objects matching the given class
            otherwise all objects from the
            database
        """
        models = {"State": State,
                  "City": City,
                  "Place": Place,
                  "Review": Review,
                  "User": User,
                  "Amenity": Amenity}
        my_dict = {}
        objects = []

        if (cls and cls.__name__ in models):
            models = {"model": models.get(cls.__name__)}

        for key, value in models.items():
            objs = self.__session.query(value)
            for obj in objs:
                objects.append(obj)

        for obj in objects:
            my_dict[f"{obj.__class__.__name__}.{obj.id}"] = obj

        return (my_dict)

    def new(self, obj):
        """
        Adds the given object to the database

        Parameters
            obj : class
            The instance to be stored
        """
        self.__session.add(obj)

    def save(self):
        """ Commits changes to database """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes the given object from the database

        Parameters
            obj : class, optional
            The instance to delete. By default,
            None is provided
        """
        if (obj):
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in the database """

        Base.metadata.create_all(self.__engine)

        session = sessionmaker(self.__engine,
                               expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        """ Close """
        self.__session.remove()