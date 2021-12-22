#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
''' from os import environ
environ['HBNB_TYPE_STORAGE'] = 'db'

if environ.get('HBNB_TYPE_STORAGE') == "db":
	from models.engine.db_storage import DBStorage
else: '''
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
