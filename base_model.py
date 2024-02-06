#!/usr/bin/python3
""" the base class of all our models. """


import uuid
import datetime


class BaseModel:
    """ Base Model class
    Attrs:
        id: string assigned by uuid.uuid4
        created_at: datetime when created
        updated_at: datetime when created and when updated
    Methods:
        save: update updated_at with current time
        to_dict: returns keys and values of the instance
    """

    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates the instance
        only updated_at is updated
        """
        self.updated_at = datetime.datetime.utcnow()

    def to_dict(self):
        """ return a dictionary with all the attributes, a class name item
        and dates converted to string format in ISO format
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        return new_dict
