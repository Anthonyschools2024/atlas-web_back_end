#!/usr/bin/env python3
""" 4. MRU Caching
"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRUCache defines a MRU (Most Recently Used) caching system
        that inherits from BaseCaching.
    """

    def __init__(self):
        """ Initialize the class.
        """
        super().__init__()
        self.usage_order = []  # To keep track of the order of usage for MRU

    def _mark_as_used(self, key):
        """ Marks a key as most recently used.
            Moves the key to the end of the usage_order list.
        """
        if key in self.usage_order:
            self.usage_order.remove(key)
        self.usage_order.append(key)

    def put(self, key, item):
        """ Add an item in the cache using MRU algorithm.
            If key or item is None, this method should not do anything.
            If the number of items in self.cache_data is higher
            than BaseCaching.MAX_ITEMS, you must discard the most
            recently used item (MRU algorithm) and print DISCARD: <key>.
        """
        if key is None or item is None:
            return

        key_exists = key in self.cache_data

        # If the key is new AND the cache is already at max capacity,
        # an eviction is needed. The item to evict is the current MRU.
        if not key_exists and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.usage_order:  # Ensure there's something to discard
                mru_key_to_evict = self.usage_order.pop()  # Get current MRU
                del self.cache_data[mru_key_to_evict]
                print(f"DISCARD: {mru_key_to_evict}")

        # Add or update the item in the cache
        self.cache_data[key] = item
        # Mark the current key (new or updated) as the most recently used
        self._mark_as_used(key)


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
