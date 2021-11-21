#!/usr/bin/python3
"""A base model class"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """ A class BaseModel that defines all common attributes/method 
    for other classes """
    id = str(uuid.uuid4())
    created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
    updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def __init__(self, *args, **kwargs):
        """constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
            models.storage.new(self)

    def __str__(self):
        """ String representation"""
        return self.__class__.__name__, self.id,\
        self.__dict__.__format__("{:s} {:s} {}")

    def save(self):
        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        to_dict = dict(self.__dict__)
        to_dict['__class__'] = self.__class__.__name__
        to_dict['updated_at'] = self.updated_at\
        .strftime("%Y-%m-%dT%H:%M:%S.%f")
        to_dict['created_at'] = self.created_at\
        .strftime("%Y-%m-%dT%H:%M:%S.%f")
        return to_dict
