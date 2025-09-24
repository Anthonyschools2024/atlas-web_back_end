#!/usr/bin/env python3
"""
A module that defines a FIFO caching system.
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    A FIFO (First-In, First-Out) caching system that inherits from
    BaseCaching.

    It discards the oldest item when the cache reaches its maximum size.
    """

    def __init__(self):
        """
        Initializes the cache.
        """
        super().__init__()

    def put(self, key, item):
        """
        Assigns an item to the cache dictionary.

        If the cache is full, it discards the first item added (FIFO).

        Args:
            key: The key for the item to be stored.
            item: The value of the item to be stored.
        """
        if key is None or item is None:
            return

        # Add item to the cache
        self.cache_data[key] = item

        # Check if cache size exceeds the limit
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Get the first key inserted (oldest item)
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            # Remove the oldest item from the cache
            del self.cache_data[first_key]

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
