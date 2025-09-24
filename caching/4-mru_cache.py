#!/usr/bin/env python3
"""
A module that defines a MRU caching system.
"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    A MRU (Most Recently Used) caching system that inherits from
    BaseCaching.

    It discards the most recently used item when the cache is full.
    """

    def __init__(self):
        """
        Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assigns an item to the cache dictionary.

        If the cache is full, it discards the most recently used item.

        Args:
            key: The key for the item to be stored.
            item: The value of the item to be stored.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        
        self.cache_data[key] = item
        
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """
        Retrieves an item from the cache by its key.

        Marks the retrieved item as the most recently used.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key, or None if the key is None
            or if the key does not exist in the cache.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
