#!/usr/bin/python3
""" Defines a function"""


def is_kind_of_class(obj, a_class):
    """ Function checks an instance of a class"""
    if isinstance(obj, a_class):
        return True
    return False
