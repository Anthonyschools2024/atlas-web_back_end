#!/usr/bin/env python3
"""
This module defines the DB class for database interactions.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """
    DB class to handle database connection and session management.
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance. It sets up the engine and creates
        all tables based on the Base metadata.
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoized session object. Creates a new session if one does not exist.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Adds a new user to the database.

        Args:
            email (str): The user's email address.
            hashed_password (str): The user's hashed password.

        Returns:
            User: The newly created user object.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Finds a user by the given keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments to filter by (e.g., email).

        Returns:
            User: The first user object matching the criteria.

        Raises:
            NoResultFound: If no user is found with the given criteria.
        """
        user = self._session.query(User).filter_by(**kwargs).one()
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Updates a user's attributes based on their ID.

        Args:
            user_id (int): The ID of the user to update.
            **kwargs: Arbitrary keyword arguments with new attribute values.

        Raises:
            ValueError: If an argument in kwargs is not a valid user attribute.
        """
        try:
            user = self.find_user_by(id=user_id)
        except NoResultFound:
            return

        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError
            setattr(user, key, value)

        self._session.commit()
