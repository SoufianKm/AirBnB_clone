#!/usr/bin/python3
"""
a unique FileStorage instance for our application
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
