#!/usr/bin/env python3
"""
Module for implementing a Cache class with Redis.
"""
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


class Cache:
    """
    A class for caching data in Redis.

    This class initializes a connection to a Redis server, flushes the database
    on initialization, and provides methods to store data with a randomly
    generated key, and retrieve data, optionally converting it to its
    original type.
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

    def get(self,
            key: str,
            fn: Optional[Callable[[bytes], Any]] = None
            ) -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis and optionally converts it.

        Args:
            key (str): The key of the data to retrieve.
            fn (Optional[Callable[[bytes], Any]]): An optional callable
                to convert the retrieved byte string data to the desired format.
                If None, the raw byte string is returned.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data, possibly
            converted by `fn`, or None if the key does not exist.
        """
        data_bytes: Optional[bytes] = self._redis.get(key)
        if data_bytes is None:
            return None

        if fn is not None:
            return fn(data_bytes)
        return data_bytes

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves data from Redis and converts it to a UTF-8 string.

        Args:
            key (str): The key of the data to retrieve.

        Returns:
            Optional[str]: The retrieved data as a string, or None if
            the key does not exist or data cannot be decoded.
        """
        value = self.get(key, fn=lambda d: d.decode("utf-8"))
        return value if isinstance(value, str) or value is None else None

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves data from Redis and converts it to an integer.

        Args:
            key (str): The key of the data to retrieve.

        Returns:
            Optional[int]: The retrieved data as an integer, or None if
            the key does not exist or data cannot be converted to int.
        """
        value = self.get(key, fn=int)
        return value if isinstance(value, int) or value is None else None
