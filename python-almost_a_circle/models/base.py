#!/usr/bin/python3
"""base"""


class Base():
    """base class for checking the id for others class"""

    
    __nb_objects = 0


    def _init_(self,id=None):
        """initialization base class with id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
