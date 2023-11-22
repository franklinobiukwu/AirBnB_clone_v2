#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from os import environ

storage_type = environ.get('HBNB_TYPE_STORAGE')
storage = None

print('Initialize')
if storage_type == 'db':
    print('Im on the database')
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    print('Im in the filestorage')
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
