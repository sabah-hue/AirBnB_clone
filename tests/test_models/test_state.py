#!/usr/bin/python3
""" model test for State class """
from models.base_model import BaseModel
import unittest
from models.review import State


class TestClassState(unittest.TestCase):
    """ test for state class by unittest """
    def test_base_class(self):
        """ baseModel is the parent """
        self.assertTrue(issubclass(State, BaseModel)) 
