#!/usr/bin/python3
""" Defined State class which inherits from Base class """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


""" map class to inherit from Base"""


class State(Base):
    """mapped class definiti"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all")
