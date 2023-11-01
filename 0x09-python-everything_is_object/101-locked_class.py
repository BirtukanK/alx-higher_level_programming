#!/usr/bin/python3
"""Define Locked class"""


class LockedClass:
    """class to prevent dynamic class attribute creation"""
    __slots__ = ['first_name']
