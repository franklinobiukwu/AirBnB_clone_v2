#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""


from os import environ

storage_type = environ.get('HBNB_TYPE_STORAGE')
storage = None

if storage_type == 'db':
    print("Of the DB!!")
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    print("Of the FileStorage")
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
