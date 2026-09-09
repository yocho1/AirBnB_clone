#!/usr/bin/python3
"""Defines the BaseModel class."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Args:
            *args: Unused.
            *kwargs: Key/value pairs of attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__
        )

    def save(self):
        """Update updated_at with the current datetime and save to storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
