#!/usr/bin/python3
"""Test cases for class User"""

from unittest import TestCase
from models.user import User
from models.base_model import BaseModel
import pycodestyle


class Test_syntax(TestCases):
    """
    Test the pycodestyle and syntax requirements
    for the `User` class
    """

    def test_pycodestyle(self):
        """
        Check the syntax from the `pycodestyle` branch
        following the Peep8 standards.
        """
        result = pycodestyle.StyleGuide(quiet=True).check_files([
            'models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style error or warnings were detected.")


class Test_User(TestCase):
    """Test class User"""

    def Test_instance(self):
        """Test instance of User class"""
        inst_user = User()
        self.assertTrue(isinstance(inst_user, User))
