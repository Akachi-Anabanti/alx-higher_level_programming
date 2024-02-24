#!/usr/bin/python3
"""Defines the database model object"""
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship
from relationship_city import City, Base


class State(Base):
    """State model class inherits from
    declarative base"""
    __tablename__ = "states"
    id = Column(Integer, Sequence('state_id_seq'), primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state',
                          cascade='all, delete-orphan')
