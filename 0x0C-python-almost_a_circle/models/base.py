#!/usr/bin/python3
""" Defines the Base class"""
import json


class Base:
    """ A class to define id of an object"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ A constructor for Base class
        Args:
            id (int): integer value
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ static method that returns JSON string format"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ class method that writes JSON format of a file"""
        f = cls.__name__ + ".json"
        with open(f, "w") as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                jfile.write(Base.to_json_string(list_dicts))
