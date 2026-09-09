#!/usr/bin/python3
"""Package initialization for models"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
