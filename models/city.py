#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """The City class that inherits from the BaseModel"""
    state_id = ""
    name = ""
