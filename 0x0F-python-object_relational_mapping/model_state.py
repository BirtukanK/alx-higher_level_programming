#!/usr/bin/python3
""" Defines State class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys
import MySQLdb

Base = declarative_base()
class State(Base):
    """ State class tht inherits from Base class"""
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
