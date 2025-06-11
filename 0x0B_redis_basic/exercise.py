#!/usr/bin/env python3
"""
Module for implementing a Cache class with Redis.
"""
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method in the Cache class is called.

    It uses the method's qualified name as the key in Redis to store the count.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The wrapped method with call counting functionality.
    """
    key_template = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        Wrapper function that increments the call count in Redis and then
        calls the original method.

        'self' is expected to be an instance of a class with a `_redis`
        attribute that is a Redis client instance (e.g., the Cache class).
        """
        if hasattr(self, '_redis') and isinstance(self._redis, redis.Redis):
            self._redis.incr(key_template)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a particular function.

    Every time the original function is called, it adds its input parameters
    to one list in Redis and stores its output into another list.
    The keys are based on the decorated function's qualified name.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The wrapped method with input/output history logging.
    """
    inputs_key = method.__qualname__ + ":inputs"
    outputs_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        Wrapper function that logs input arguments and output to Redis lists.

        'self' is expected to be an instance of a class with a `_redis`
        attribute that is a Redis client instance (e.g., the Cache class).
        Input arguments are stored as str(args).
        """
        # For simplicity as per instructions, only positional args are logged.
        # kwargs are ignored for history logging but passed to original method.
        if hasattr(self, '_redis') and isinstance(self._redis, redis.Redis):
            self._redis.rpush(inputs_key, str(args))

        output = method(self, *args, **kwargs)

        if hasattr(self, '_redis') and isinstance(self._redis, redis.Redis):
            self._redis.rpush(outputs_key, output)
        return output
    return wrapper


class Cache:
    """
    A class for caching data in Redis.

    This class initializes a connection to a Redis server, flushes the database
    on initialization, and provides methods to store data with a randomly
    generated key, and retrieve data, optionally converting it to its
    original type. Methods can be decorated to count their calls and log
    their input/output history.
    """
    def __init__(self) -> None:
        """
        Initializes the Cache instance.

        This method creates a private Redis client instance and flushes
        the Redis database associated with that instance.
        """
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis using a random key.
        The number of times this method is called is tracked in Redis.
        The history of its inputs and outputs is also logged to Redis lists.

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
        # Ensure the return type strictly matches Optional[str]
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
        # Ensure the return type strictly matches Optional[int]
        return value if isinstance(value, int) or value is None else None
