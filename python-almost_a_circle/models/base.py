#!/usr/bin/python3
"""base module cotains class base"""


class Base():
    """base class for checking the id for others class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization base class with id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
