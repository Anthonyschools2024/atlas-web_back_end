#!/usr/bin/env python3
"""
Module for implementing a Cache class with Redis.
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


class Cache:
    """
    A class for caching data in Redis.

    This class initializes a connection to a Redis server, flushes the database
    on initialization, and provides a method to store data with a randomly
    generated key.
    """
    def __init__(self) -> None:
        """
        Initializes the Cache instance.

        This method creates a private Redis client instance and flushes
        the Redis database associated with that instance.
        """
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis using a random key.

        Args:
            data: The data to be stored. Can be of type str, bytes,
                  int, or float.

        Returns:
            str: The randomly generated key (UUID) under which the data
                 is stored in Redis.
        """
        random_key: str = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
