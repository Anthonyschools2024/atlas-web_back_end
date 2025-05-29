#!/usr/bin/env python3
"""
Module for hypermedia pagination.
Contains the Server class, index_range function, and get_hyper method.
"""

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end index for a given page and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset.

        Args:
            page (int): The page number to retrieve (1-indexed). Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            List[List]: A list of rows corresponding to the requested page.
                        Returns an empty list if arguments are out of range.
        """
        assert isinstance(page, int) and page > 0, \
            "page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be an integer greater than 0"

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()

        if start_index >= len(data):
            return

        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Retrieves a page of data and hypermedia pagination details.

        Args:
            page (int): The page number to retrieve (1-indexed). Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            Dict[str, Any]: A dictionary containing pagination details.
        """
        # Assertions for page and page_size are handled by get_page
        data_page = self.get_page(page, page_size)
        
        total_items = len(self.dataset())
        # page_size is asserted > 0 in get_page, so no division by zero
        total_pages = math.ceil(total_items / page_size)

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None
        
        # If current page requested is beyond total_pages, data_page will be empty
        # and next_page should be None.
        if page >= total_pages and data_page ==: # Handles cases like page 3000 for 195 total pages
             next_page = None


        hyper_data = {
            "page_size": len(data_page),
            "page": page,
            "data": data_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
        return hyper_data
