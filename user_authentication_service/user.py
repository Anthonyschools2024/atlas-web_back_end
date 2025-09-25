#!/usr/bin/env python3
"""
This module defines the SQLAlchemy User model.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """
    Represents a user in the database.

    This SQLAlchemy model maps to the 'users' table and defines the
    schema for storing user information, including credentials and
    session details.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
