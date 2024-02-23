#!/usr/bin/python3
"""Defines the database model object"""
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """City model class inherits from
    declarative base"""
    __tablename__ = "cities"
    id = Column(Integer, Sequence('city_id_seq'), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
