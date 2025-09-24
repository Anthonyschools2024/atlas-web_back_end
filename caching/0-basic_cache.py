#!/usr/bin/env python3
"""
A module that defines a basic caching system.
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A basic caching system that inherits from BaseCaching.

    This caching system has no limit on the number of items it can store.
    """

    def put(self, key, item):
        """
        Assigns an item to the cache dictionary.

        This method does nothing if the key or item is None.

        Args:
            key: The key for the item to be stored.
            item: The value of the item to be stored.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache by its key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key, or None if the key is None
            or if the key does not exist in the cache.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
