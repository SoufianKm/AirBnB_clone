#!/usr/bin/python3
""" the base class of all our models. """
import uuid
from datetime import datetime
import models


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

    def __init__(self, *args, **kwargs):
        """
        Constructor of the class BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key != "created_at" and key != "updated_at":
                    self.__dict__[key] = value
                else:
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            models.storage.new(self)

    def __str__(self):
        """
        print:
            [<class name>] (<self.id>) <self.__dict__>

        Return:
            description with the information changed
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        updates the instance only updated_at is updated
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        return a dictionary with all the attributes, a class name item
        and dates converted to string format in ISO format
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["updated_at"] = self.created_at.isoformat()
        new_dict["created_at"] = self.updated_at.isoformat()
        return new_dict
