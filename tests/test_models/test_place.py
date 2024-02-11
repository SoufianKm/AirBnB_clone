#!/usr/bin/python3
"""Test cases for class Place"""

from unittest import TestCase
from models.place import Place
from models.base_model import BaseModel
import pycodestyle


class Test_syntax(TestCases):
    """
    Test the pycodestyle and syntax requirements
    for the `Place` class
    """

    def test_pycodestyle(self):
        """
        Check the syntax from the `pycodestyle` branch
        following the Peep8 standards.
        """
        result = pycodestyle.StyleGuide(quiet=True).check_files([
            'models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style error or warnings were detected.")


class Test_Place(TestCase):
    """Test class Place"""

    def Test_instance(self):
        """Test instance of Place class"""
        inst_place = Place()
        self.assertTrue(isinstance(inst_place, Place))
