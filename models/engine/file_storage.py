#!/usr/bin/python3
"""
FileStorage class module
"""
import json
import sys
from models.base_model import BaseModel


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
                for value in dicts.values():
                    my_obj = BaseModel(**value)
                    self.new(my_obj)
        except json.decoder.JSONDecodeError:
            with open(self.__file_path, mode='w') as f:
                f.write('{}')
        except PermissionError:
            raise PermissionError('no read permission on file.json')

    def delete(self, key):
        """deletes one item form __objects"""
        self.__objects.update({key: "safe delete"})
        self.__objects.pop(key)
