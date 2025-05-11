#!/usr/bin/env python3
"""
This module contains a type-annotated function 'floor'.
"""

import math


def floor(n: float) -> int:
    """
    Calculates the floor of a floating-point number.

    Args:
        n (float): The float number.

    Returns:
        int: The floor of n, as an integer.
    """
    return math.floor(n)
