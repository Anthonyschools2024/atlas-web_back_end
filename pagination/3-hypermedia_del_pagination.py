#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Optional

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes the Server instance.
        Sets dataset and indexed_dataset to None initially.
        """
        self.__dataset: Optional[List[List[str]]] = None
        self.__indexed_dataset: Optional[Dict[int, List[str]]] = None


    def dataset(self) -> List[List[str]]:
        """Cached dataset
        Loads the dataset from the CSV file if not already loaded.
        Skips the header row.

        Returns:
            List[List[str]]: The dataset as a list of rows (list of strings).
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding='utf-8') as f: # Ensure correct encoding
                reader = csv.reader(f)
                dataset_from_csv = [row for row in reader]
            self.__dataset = dataset_from_csv[1:]  # Skip header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Dataset indexed by sorting position, starting at 0
        Creates an indexed version of the dataset for quick lookups.
        The keys are the original 0-based indices of the rows.

        Returns:
            Dict[int, List[str]]: The dataset indexed by original position.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # The full dataset is indexed.
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """
        Retrieves a page of data using index-based pagination,
        resilient to deletions from the indexed dataset.

        Args:
            index (int, optional): The start index of the page (0-indexed).
                                   Defaults to 0 if None.
            page_size (int): The number of items requested per page.
                             Defaults to 10.

        Returns:
            Dict: A dictionary containing pagination details:
                - index (int): The starting index for the current page's data.
                - next_index (Optional[int]): The starting index for the next page,
                                              or None if no next page.
                - page_size (int): The originally requested number of items per page.
                - data (List[List[str]]): The list of rows for the current page.
        """
        # Determine the actual starting index for the current page
        current_page_start_index = index if index is not None else 0

        # Load the full dataset to get its total length for assertion
        original_dataset_length = len(self.dataset())

        # Assert that the effective starting index is a non-negative integer
        # and is less than the total number of items in the original dataset.
        assert isinstance(current_page_start_index, int) and \
            0 <= current_page_start_index < original_dataset_length, \
            "Requested index is out of range."

        # Ensure the indexed dataset is loaded
        indexed_data = self.indexed_dataset()

        data_page_content: List[List[str]] = []
        items_collected_count: int = 0
        
        current_lookup_key: int = current_page_start_index
        
        # Loop until we have collected enough items for the page or
        # we have checked all possible original indices up to the end of the dataset.
        while items_collected_count < page_size and \
              current_lookup_key < original_dataset_length:
            
            item = indexed_data.get(current_lookup_key)
            
            if item is not None: # Item exists at this original index (not deleted)
                data_page_content.append(item)
                items_collected_count += 1
            
            current_lookup_key += 1 # Move to the next logical original index

        # Determine the next_index for the client to query.
        next_page_start_index = current_lookup_key \
            if current_lookup_key < original_dataset_length else None

        return {
            "index": current_page_start_index,
            "data": data_page_content,
            "page_size": page_size, # Return the requested page_size as per task
            "next_index": next_page_start_index
        }
