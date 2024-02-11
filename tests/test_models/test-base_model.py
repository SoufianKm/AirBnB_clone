#!/usr/bin/python3
"""
Unittest for base_model class
"""
from datetime import date, datetime
from unittest import TestCase
from models import base_model
import uuid
import pycodestyle


class Test_syntax(TestCases):
    """
    Test the pycodestyle and syntax requirements
    for the `base_model` class
    """

    def test_pycodestyle(self):
        """
        Check the syntax from the `pycodestyle` branch
        following the Peep8 standards.
        """
        result = pycodestyle.StyleGuide(quiet=True).check_files([
            'models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style error or warnings were detected.")


class Test_BaseModel(TestCase):
    """Test class BaseModel"""

    def test_instance_method(self):
        """Test that the BaseModel instance contains identical methods"""
        bm = dir(BaseModel())
        self.assertIn('__init__', bm)
        self.assertIn('save', bm)
        self.assertIn('to_dict', bm)
        self.assertIn('__str__', bm)

    def Test_instance(self):
        """Test the instance of BaseModel"""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime.datetime)
        self.assertIsInstance(bm.updated_at, datetime.datetime)
        self.assertIsInstance(bm.__class__, type)

    def Test_instantiation_with_kwargs(self):
        """Test instantiation with kwargs"""
        bm = BaseModel()
        dictionary = bm.to_dict()
        new_date = datetime.today()
        new_date_iso = new_date.isoformat()
        dictionary["created_at"] = new_date_iso
        dictionary["updated_at"] = new_date_iso
        id = dictionary["id"]
        bm = BaseModel(**dictionary)
        self.assertEqual(bm.id, id)
        self.assertEqual(bm.created_at, new_date)
        self.assertEqual(bm.updated_at, new_date)

    def Test_id_value(self):
        """Verify whether the `id` is a UUID version 4."""
        bm = BaseModel(id='1')
        with self.assertRaises(ValueError) as _:
            uuid.UUID(bm.id, version=4)
        bm2 = BaseModel(id=['1'])
        with self.assertRaises(AttributeError) as _:
            uuid.UUID(bm2.id, version=4)

    def Test_save(self):
        """Test if updated_at is changed with save method"""
        bm = BaseModel()
        bm.save()
        self.assertNotEqual(
                bm.__dict__['updated_at'],
                bm.__dict__['updated_at'])
        models.storage.reload()
        self.assertEqual(bm.__dict__['updated_at'], bm.__dict__['updated_at'])

    def Test_to_dict(self):
        """Test to_dict method"""
        bm = BaseModel()
        bm.name = "ALX"
        for k, v in ba.__dict__.items():
            if k != 'updated_at' and k != 'created_at':
                self.assertIn(k, bm.to_dict())
                self.assertEqual(v, bm.to_dict()[k])
        self.assertEqual(bm.to_dict()['__class__'], bm.__class__.__name__)
        self.assertEqual(bm.to_dict()['updated_at'], bm.updated_at.isoformat())
        self.assertEqual(bm.to_dict()['created_at'], bm.created_at.isoformat())
        self.assertEqual(bm.to_dict()['name'], 'ALX')
        self.assertIsInstance(bm.to_dict(), dict)

    def Test_str(self):
        """Test __str__ method"""
        bm = BaseModel()
        string = '['+bm.__class__.__name__+']'+' ('+bm.id+') '+str(bm.__dict__)
        self.assertEqual(string, bm.__str__())
