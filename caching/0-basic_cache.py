#!/usr/bin/env python3
""" 0. Basic dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache defines a basic caching system
        that inherits from BaseCaching.
        This caching system doesn't have a limit.
    """

    def put(self, key, item):
        """ Add an item in the cache.
            If key or item is None, this method should not do anything.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key.
            If key is None or if the key doesn’t exist in self.cache_data,
            return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
