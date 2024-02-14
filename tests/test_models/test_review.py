#!/usr/bin/python3
""" model test for review class """
from models.base_model import BaseModel
import unittest
from models.review import Review


class TestlassState(unittest.TestCase):
    """ test for review class by unittest """
     def test_base_class(self):
         """ baseModel is the parent """
         self.assertTrue(issubclass(Review, BaseModel))
