#!/usr/bin/python3
""" model test for amenity class """
from models.base_model import BaseModel
import unittest
from models.amenity import Amenity


class TestClassUser(unittest.TestCase):
    """ test case for amenity class by unittest """
     def test_sub_class(self):
         """ test if basemodel is parent """
         self.assertTrue(issubclass(Amenity, BaseModel))
