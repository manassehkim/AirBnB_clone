#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models

"""
Module BaseModel
Parent of all classes

"""

class BaseModel():
    """Base class for AirBnB clone project 
    methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """
    def __init__(self, *args, **kwargs):
        """
        Initializing random attributes: random uuid, dates created/updated

        """

        if kwargs:
            for key, val in kwargs.items():
                if "created_at" = key:
                    self.created_at = datetime.strtime(kwargs["created_at"],
                            "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strtime(kwargs["updated_at"],
                            "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return String information about model

        """
        return('[{}]({}){}'.
                format(self.__class__.__name__, self.id, self.__dict__))
    def __repr__(self):
        """
        Return String representation

        """
        return(self.__str__())
    def save(self):
        """
        Update instance with uodated time and save to serialized file

        """
        self.updated_at = datetime.now()
        model.storage.save()

    def to_dict(self):
        """
        Return dictionary with string formats of times;
        add class info to dictionary.

        """
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, v in self.dict__.items():
            if isinstance(v, (datetime, )):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic

