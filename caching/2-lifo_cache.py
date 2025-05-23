#!/usr/bin/env python3
""" 2. LIFO Caching
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache defines a LIFO caching system
        that inherits from BaseCaching.
    """

    def __init__(self):
        """ Initialize the class.
        """
        super().__init__()
        self.order_of_keys = []  # To keep track of the order of keys for LIFO

    def put(self, key, item):
        """ Add an item in the cache using LIFO algorithm.
            If key or item is None, this method should not do anything.
            If the number of items in self.cache_data is higher
            than BaseCaching.MAX_ITEMS, you must discard the last
            item put in cache (LIFO algorithm) and print DISCARD: <key>.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If key already exists, update its value and its position in order_of_keys
            self.cache_data[key] = item
            self.order_of_keys.remove(key) # Remove to re-add at the end
            self.order_of_keys.append(key)
            return

        # Key is new
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Cache is full (or will be), and we are adding a new key
            if self.order_of_keys: # Make sure there's something to discard
                last_in_key = self.order_of_keys.pop()  # Get the last item added
                del self.cache_data[last_in_key]
                print(f"DISCARD: {last_in_key}")

        self.cache_data[key] = item
        self.order_of_keys.append(key)


    def get(self, key):
        """ Get an item by key.
            If key is None or if the key doesn’t exist in self.cache_data,
            return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
