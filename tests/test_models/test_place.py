#!/usr/bin/python3
""" model test for place class """
from models.base_model import BaseModel
import unittest
from models.place import Place


class TestClassPlace(unittest.TestCase):
    """ test case for place class by unittest """
     def test_sub_class(self):
         """ test if basemodel is parent """
         self.assertTrue(issubclass(Place, BaseModel))
