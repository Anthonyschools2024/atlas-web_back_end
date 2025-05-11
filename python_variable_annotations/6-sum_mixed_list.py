#!/usr/bin/env python3
"""
This module contains a type-annotated function 'sum_mixed_list'.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing both integers and floats.

    The sum is returned as a float.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats to sum.

    Returns:
        float: The sum of the numbers in mxd_lst.
    """
    return sum(mxd_lst)
