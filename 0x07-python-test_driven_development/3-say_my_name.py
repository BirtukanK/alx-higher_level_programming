#!/usr/bin/python3
"""Defines a function"""


def say_my_name(first_name, last_name=""):
    """
    Function printing My name is <first name> <last name>

    Args:
        first_name (str): first name
        lasst_name (str): second name

    Raises:
        TypeError
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
