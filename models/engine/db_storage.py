#!/usr/bin/python3
"""Module for Database Storage"""
from os import environ
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.base_model import Base
from sqlalchemy import create_engine

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

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user,
                                              password,
                                              host,
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
        print('ENTER THE ALL BLOCK')
        
        if cls is not None:
            print("HAS CLASS NAME")
            print(cls)
            objects = self.__session.query(cls).all()
        else:
            print('CLASS IN NONE')
            objects = []
            for classes in clsname_dict.values():
                objects.append(self.__session.query(classes).all())
        print('******************')
        print(objects)
        print("******************")
        for obj in objects:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            value = obj
            new_dict[key] = value
            
        print('ABOUT TO RETURN')
        print("--------------------------------------")
        print(new_dict)
        print("--------------------------------------")
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

        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
