#!/usr/bin/python3
""" Defines the Base class"""


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
