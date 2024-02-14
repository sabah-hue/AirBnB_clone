#!/usr/bin/python3
""" model for review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ class for review wich inherete from BaseModel """
    place_id = ""
    user_id = ""
    text = ""
