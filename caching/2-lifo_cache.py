#!/usr/bin/env python3
"""
A module that defines a LIFO caching system.
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    A LIFO (Last-In, First-Out) caching system that inherits from
    BaseCaching.

    It discards the most recently added item when the cache is full.
    """

    def __init__(self):
        """
        Initializes the cache.
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns an item to the cache dictionary.

        If the cache is full, it discards the last item added (LIFO).

        Args:
            key: The key for the item to be stored.
            item: The value of the item to be stored.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
           key not in self.cache_data:
            # Pop the last item added
            last_key, _ = self.cache_data.popitem()
            print(f"DISCARD: {last_key}")

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
