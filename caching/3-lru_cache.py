#!/usr/bin/env python3
""" 3. LRU Caching
"""

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """ LRUCache defines a LRU caching system
        that inherits from BaseCaching.
    """

    def __init__(self):
        """ Initialize the class.
        """
        super().__init__()
        self.usage_order = []  # To keep track of the order of usage for LRU

    def _mark_as_used(self, key):
        """ Marks a key as most recently used.
            Moves the key to the end of the usage_order list.
        """
        if key in self.usage_order:
            self.usage_order.remove(key)
        self.usage_order.append(key)

    def put(self, key, item):
        """ Add an item in the cache using LRU algorithm.
            If key or item is None, this method should not do anything.
            If the number of items in self.cache_data is higher
            than BaseCaching.MAX_ITEMS, you must discard the least
            recently used item (LRU algorithm) and print DISCARD: <key>.
        """
        if key is None or item is None:
            return

        # If key is new and cache is full, perform eviction
        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.usage_order:  # Ensure there's something to discard
                lru_key = self.usage_order.pop(0)  # Least recently used is at the start
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self._mark_as_used(key)  # Mark current key as most recently used

    def get(self, key):
        """ Get an item by key.
            If key is None or if the key doesn’t exist in self.cache_data,
            return None.
            Accessing a key marks it as most recently used.
        """
        if key is None or key not in self.cache_data:
            return None

        # Mark the accessed key as most recently used
        self._mark_as_used(key)
        return self.cache_data.get(key)
