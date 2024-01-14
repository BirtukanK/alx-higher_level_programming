#!/usr/bin/python3
""" Defines City class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import sys
import MySQLdb
from model_state import Base, State
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """ City class that inherits from Base class"""
    __tablename__ = 'cities'
    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
