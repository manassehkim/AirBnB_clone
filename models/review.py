#!/usr/bin/python3
"""
Review class module

"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Inherits from BaseModel
    Public class attributes:
    (i) place_id:   (str) will be place.id
    (ii) user_id:   (str) will be user.id
    (iii) text:     (str)

    """
    place_id = ""
    user_id = ""
    text = ""
