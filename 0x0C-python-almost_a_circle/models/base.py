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

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Class method returns an istance with all attributes
        already set

        Args:
            cls - to access the class method
            dictionary (dict) - pointer to a dictionary 
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
