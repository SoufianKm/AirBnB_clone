#!/usr/bin/python3
"""Test cases for class Amenity"""

from unittest import TestCase
from models.amenity import Amenity
from models.base_model import BaseModel
import pycodestyle


class Test_syntax(TestCase):
    """
    Test the pycodestyle and syntax requirements
    for the `Amenity` class
    """

    def test_pycodestyle(self):
        """
        Check the syntax from the `pycodestyle` branch
        following the Peep8 standards.
        """
        result = pycodestyle.StyleGuide(quiet=True).check_files([
            'models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style error or warnings were detected.")


class Test_Amenity(TestCase):
    """Test class Amenity"""

    def Test_instance(self):
        """Test instance of Amenity class"""
        inst_amenity = Amenity()
        self.assertTrue(isinstance(inst_amenity, Amenity))
