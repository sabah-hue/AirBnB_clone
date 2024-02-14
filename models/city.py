#!/usr/bin/python3
""" model  for city class """
from models.base_model import BaseModel


class City(BaseModel):
    """ city class which inherite from baseModel """
    state_id = ""
    name = ""
