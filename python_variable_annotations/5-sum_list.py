#!/usr/bin/env python3
"""
This module contains a type-annotated function 'sum_list'.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): The list of floats to sum.

    Returns:
        float: The sum of the floats in input_list.
    """
    return sum(input_list)
