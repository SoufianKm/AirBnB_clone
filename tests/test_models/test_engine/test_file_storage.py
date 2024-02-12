#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
import pep8
import json
import sys
from os import path, remove
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import pycodestyle


class Test_syntax(TestCase):
    """
    Test the pycodestyle and syntax requirements
    for the `FileStorage` class
    """

    def test_pycodestyle(self):
        """
        Check the syntax from the `pycodestyle` branch
        following the Peep8 standards.
        """
        result = pycodestyle.StyleGuide(quiet=True).check_files([
            'models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style error or warnings were detected.")


class Test_File_Storage(TestCase):
    """Test FileStorage class"""

    def setUp(self):
        """
        Resetting private class attributes __file_path
        and __objects to default values 'file.json'
        and {} before each test
        """
        FileStorage._FileStorage__file_path = 'file.json'
        FileStorage._FileStorage__objects = {}

    def test_class_method(self):
        """Test that FileStorage methods existance"""
        fs = dir(FileStorage)
        self.assertIn('all', fs)
        self.assertIn('new', fs)
        self.assertIn('save', fs)
        self.assertIn('reload', fs)

    def test_class_attribute(self):
        """Test FileStorage attributes existance"""
        fs = dir(FileStorage)
        self.assertIn('_FileStorage__file_path', fs)
        self.assertIn('_FileStorage__objects', fs)

    def test_instance_method(self):
        """Test FileStorage instance if contains identical methods"""
        fs = dir(FileStorage())
        self.assertIn('all', fs)
        self.assertIn('new', fs)
        self.assertIn('save', fs)
        self.assertIn('reload', fs)

    def test_instance_attribute(self):
        """Test FileStorage instance if has identical attributes"""
        fs = dir(FileStorage())
        self.assertIn('_FileStorage__file_path', fs)
        self.assertIn('_FileStorage__objects', fs)

    def test_docstring(self):
        """Test Module, Class, and methods all have a docstring"""
        self.assertIsNot(file_storage.__doc__, None)
        self.assertIsNot(FileStorage.__doc__, None)
        self.assertIsNot(FileStorage.all.__doc__, None)
        self.assertIsNot(FileStorage.new.__doc__, None)
        self.assertIsNot(FileStorage.save.__doc__, None)
        self.assertIsNot(FileStorage.reload.__doc__, None)

    def test_instantiation(self):
        """Test proper instantiation of object 'storage'"""

        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(FileStorage._FileStorage__file_path, 'file.json')
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def new(self, obj):
        """Test method `new`"""

        storage = FileStorage()

        bm = BaseModel()
        storage.new(bm)
        self.assertEqual(FileStorage.__objects[
            bm.__class__.__name__+'.'+bm.id], bm)

        user = User()
        storage.new(user)
        self.assertEqual(FileStorage.__objects[
            user.__class__.__name__+'.'+user.id], user)

        state = State()
        storage.new(state)
        self.assertEqual(FileStorage.__objects[
            state.__class__.__name__+'.'+state.id], state)

        city = City()
        storage.new(city)
        self.assertEqual(FileStorage.__objects[
            city.__class__.__name__+'.'+city.id], city)

        amenity = Amenity()
        storage.new(amenity)
        self.assertEqual(FileStorage.__objects[
            amenity.__class__.__name__+'.'+amenity.id], amenity)

        place = Place()
        storage.new(place)
        self.assertEqual(FileStorage.__objects[
            place.__class__.__name__+'.'+place.id], place)

        review = Review()
        storage.new(review)
        self.assertEqual(FileStorage.__objects[
            review.__class__.__name__+'.'+review.id], review)

    def test_all(self):
        """Test the all method"""

        storage = FileStorage()

        bm = BaseModel()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[
            bm.__class__.__name__+'.'+bm.id], bm)

        user = User()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[
            user.__class__.__name__+'.'+user.id], user)

        state = State()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[
            state.__class__.__name__+'.'+state.id], state)

        city = City()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[
            city.__class__.__name__+'.'+city.id], city)

        amenity = Amenity()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[
            amenity.__class__.__name__+'.'+amenity.id], amenity)

        place = Place()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[
            place.__class__.__name__+'.'+place.id], pl)

        review = Review()
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(storage.all()[
            review.__class__.__name__+'.'+review.id], review)

    def test_save(self):
        """Test the save method"""

        storage = FileStorage()

        storage.save()
        self.assertTrue(path.isfile('file.json'))
        with open("file.json") as f:
            self.assertEqual(f.read(), '{}')

        bm = BaseModel()
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())[
                bm.__class__.__name__+'.'+bm.id], bm.to_dict())

        user = User()
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())[
                user.__class__.__name__+'.'+user.id], user.to_dict())

        state = State()
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())[
                state.__class__.__name__+'.'+state.id], state.to_dict())

        city = City()
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())
                             [city.__class__.__name__+'.'+city.id],
                             city.to_dict())

        amenity = Amenity()
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())
                             [amenity.__class__.__name__+'.'+amenity.id],
                             amenity.to_dict())

        place = Place()
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())[
                place.__class__.__name__+'.'+place.id], place.to_dict())

        review = Review()
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        with open("file.json") as f:
            self.assertIsInstance(json.loads(f.read()), dict)
        with open("file.json") as f:
            self.assertEqual(json.loads(f.read())[
                review.__class__.__name__+'.'+review.id], review.to_dict())

    def test_reload(self):
        """Test the reload method"""

        storage = FileStorage()

        bm = BaseModel()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__objects
                              [bm.__class__.__name__+'.'+bm.id], BaseModel)
        self.assertEqual(FileStorage._FileStorage__objects
                         [bm.__class__.__name__+'.'+bm.id].to_dict(),
                         bm.to_dict())

        user = User()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__objects
                              [user.__class__.__name__+'.'+user.id], User)
        self.assertEqual(FileStorage._FileStorage__objects
                         [user.__class__.__name__+'.'+user.id].to_dict(),
                         user.to_dict())

        state = State()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__objects
                              [state.__class__.__name__+'.'+state.id], State)
        self.assertEqual(FileStorage._FileStorage__objects
                         [state.__class__.__name__+'.'+state.id].to_dict(),
                         state.to_dict())

        city = City()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__objects
                              [city.__class__.__name__+'.'+city.id], City)
        self.assertEqual(FileStorage._FileStorage__objects
                         [city.__class__.__name__+'.'+city.id].to_dict(),
                         city.to_dict())

        amenity = Amenity()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__objects[
            amenity.__class__.__name__+'.'+amenity.id], Amenity)
        self.assertEqual(FileStorage._FileStorage__objects[
            amenity.__class__.__name__+'.'+amenity.id].to_dict(),
            amenity.to_dict())

        place = Place()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__objects[
            place.__class__.__name__+'.'+place.id], Place)
        self.assertEqual(FileStorage._FileStorage__objects[
            place.__class__.__name__+'.'+place.id].to_dict(),
            place.to_dict())

        review = Review()
        storage.save()
        storage.reload()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__objects[
            review.__class__.__name__+'.'+review.id], Review)
        self.assertEqual(FileStorage._FileStorage__objects[
            reiview.__class__.__name__+'.'+review.id].to_dict(),
            review.to_dict())
