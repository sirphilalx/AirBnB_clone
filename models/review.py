#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """the place class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
