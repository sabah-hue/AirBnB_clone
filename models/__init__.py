#!/usr/bin/python3
""" FileStorage for airbnb application """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
