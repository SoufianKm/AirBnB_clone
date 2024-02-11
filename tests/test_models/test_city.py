#!/usr/bin/python3
"""Test City module"""

from unittest import TestCase
from models.city import City
from models.base_model import BaseModel
import pycodestyle


class Test_syntax(TestCases):
    """
    Test the pycodestyle and syntax requirements
    for the `City` class
    """

    def test_pycodestyle(self):
        """
        Check the syntax from the `pycodestyle` branch
        following the Peep8 standards.
        """
        result = pycodestyle.StyleGuide(quiet=True).check_files([
            'models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style error or warnings were detected.")


class Test_City(TestCase):
    """Test class City"""

    def Test_instance(self):
        """Testing instances of class City"""
        inst_city = City()
        self.assertTrue(isinstance(inst_city, City))
