#!/usr/bin/env python3
""" 1. FIFO caching
"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system
        that inherits from BaseCaching.
    """

    def __init__(self):
        """ Initialize the class.
        """
        super().__init__()
        self.queue = []  # To keep track of the order of keys

    def put(self, key, item):
        """ Add an item in the cache using FIFO algorithm.
            If key or item is None, this method should not do anything.
            If the number of items in self.cache_data is higher
            than BaseCaching.MAX_ITEMS, you must discard the first
            item put in cache (FIFO algorithm) and print DISCARD: <key>.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Cache is full, and we are adding a new key
            oldest_key = self.queue.pop(0)  # Get the first item added
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")
        elif key in self.cache_data:
            # If key already exists, update it and remove from queue to re-add later
            # to maintain its current "age" if it were a new item.
            # However, for strict FIFO, updating a key doesn't change its order.
            # The problem statement doesn't explicitly say what to do on update
            # regarding order. Standard FIFO means order is based on insertion only.
            # So, we only update the value. If it was already in queue, it stays.
            pass # Value will be updated below, order remains.

        self.cache_data[key] = item
        if key not in self.queue: # Add to queue only if it's a new key
            self.queue.append(key)
        elif key in self.queue and self.cache_data[key] != item:
            # If an existing key is updated, its order in FIFO doesn't change.
            # The queue should already contain it.
            pass


    def get(self, key):
        """ Get an item by key.
            If key is None or if the key doesn’t exist in self.cache_data,
            return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
