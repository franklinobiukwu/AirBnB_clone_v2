#!/usr/bin/python3
"""Module for Database Storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import environ
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage():
    """Database class"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialization of class attributes"""
        user = environ.get('HBNB_MYSQL_USER')
        password = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST', default='localhost')
        database = environ.get('HBNB_MYSQL_DB')
        env = environ.get('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(user,
                                              password,
                                              database), pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Retrieve all the tables in the database
        Args:
            cls = Is the given class name to be queried
        """
        new_dict = {}

        clsname_dict = {
            "User": User,
            "State": State,
            "Review": Review,
            "Place": Place,
            "City": City,
            "Amenity": Amenity,
        }

        if cls is not None and cls not in clsname_dict:
            return new_dict

        if cls is not None:
            objects = self.__session.query(clsname_dict[cls]).all()
        else:
            objects = []
            for classes in clsname_dict.values():
                objects.append(self.__session.query(classes).all())
        for obj in objects:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            value = obj
            new_dict[key] = value

        return new_dict

    def new(self, obj):
        """ Adds new objet to the database"""
        self.__session.add(obj)

    def save(self):
        """Commits all chancges into the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database"""
        if obj is not None:
            self.__session.delete(obj)
        else:
            return

    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
