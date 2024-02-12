#!/usr/bin/python3
"""
FileStorage class module
"""
import json
import sys
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """
    a class that serializes instances to a JSON
    file and deserializes JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        function returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        function that serializes __objects to the JSON file
        (path: __file_path);
        """
        '''
        try:
            with open(self.__file_path, mode='r', encoding='UTF-8') as f:
                new_dict = json.loads(f.read())
        except:
            with open(self.__file_path, mode='w', encoding='UTF-8') as f:
                f.write('')
        '''
        new_dict = {}
        for key, obj in self.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(self.__file_path, mode='w', encoding='UTF-8') as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, mode='r') as f:
                dicts = json.load(f)
                for obj in dicts.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except (FileNotFoundError, PermissionError):
            return

    def delete(self, key):
        """deletes one item form __objects"""
        self.__objects.update({key: "safe delete"})
        self.__objects.pop(key)
