#!/usr/bin/python3
"""
Module class Place

"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Inherits from BaseModel

    public class attributes:
        i.   city_id (str) it will be City.id
        ii.  user_id (str) it will be User.id
        iii. name (str)
        iv.  description (str)
        v.   number_rooms: (int) = 0
        vi.  number_bathrooms: (int) = 0
        vii. max_guest: (int) = 0
        viii.price_by_night: (int) = 0
        ix.  latitude: (float) = 0.0
        x.   longitude: (float) = 0.0
        xi.  amenity_ids: ([str]) it be the list of Amenity.id

    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

