#!/usr/bin/python3
"""Test cases for State class"""
from unittest import TestCase
from models.state import State
from models.base_model import BaseModel
import pycodestyle


class Test_syntax(TestCase):
    """
    Test the pycodestyle and syntax requirements
    for the `State` class
    """

    def test_pycodestyle(self):
        """
        Check the syntax from the `pycodestyle` branch
        following the Peep8 standards.
        """
        result = pycodestyle.StyleGuide(quiet=True).check_files([
            'models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Code style error or warnings were detected.")


class Test_State(TestCase):
    """Test class State"""

    def Test_instance(self):
        """Test instance of State class"""
        inst_state = State()
        self.assertTrue(isinstance(inst_state, State))
