#!/usr/bin/python3
"""
city class module

"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    Inherits from BaseModel

    public class attributes:
    state_id (str) it will be State.id
    name    (str)
    """
    state_id = ""
    name = ""
