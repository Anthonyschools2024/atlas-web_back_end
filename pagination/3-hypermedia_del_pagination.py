#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # The truncated_dataset line below was in the original boilerplate
            # but is not used. The dictionary includes the full dataset.
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Gets a page of data using an index, resilient to deletions.

        Args:
            index (int): The starting index of the page. Defaults to 0.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing pagination details.
        """
        indexed_data = self.indexed_dataset()
        max_index = len(indexed_data)

        # Use 0 for the start index if None is provided
        start_index = index if index is not None else 0

        # Assert that the start_index is within a valid range
        assert isinstance(start_index, int) and 0 <= start_index < max_index

        data = []
        count = 0
        current_index = start_index

        while count < page_size and current_index < max_index:
            # Check if the current index exists in the dataset (it might be deleted)
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                count += 1
            current_index += 1

        next_index = current_index

        return {
            'index': start_index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
