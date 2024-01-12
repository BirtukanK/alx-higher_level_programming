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
    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], port=3306, host="localhost")
    cur = conn.cursor()
