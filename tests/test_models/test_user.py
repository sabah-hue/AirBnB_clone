#!/usr/bin/python3
""" model test for user class """
from models.base_model import BaseModel
import unittest
from models.user import User


class TestClassUser(unittest.TestCase):
    """ test case for user class by unittest """
     def test_sub_class(self):
         """ test if basemodel is parent """
         self.assertTrue(issubclass(User, BaseModel))
