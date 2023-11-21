#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import environ


# storage = FileStorage()
#
print("I'm initializing")

storage_type = environ.get('HBNB_TYPE_STORAGE')
storage = None

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    print("Of to DB!!")
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    print("Of to FileStorage!!")
    storage = FileStorage()

storage.reload()
