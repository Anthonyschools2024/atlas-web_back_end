#!/usr/bin/env python3
"""
This module contains a type-annotated function 'to_kv'.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple with a string k and the square of v.

    The second element of the tuple (the square of v) is annotated
    as a float in the return type. The actual runtime type of the
    squared value will be int if v is int, or float if v is float.

    Args:
        k (str): The string key.
        v (Union[int, float]): The integer or float value.

    Returns:
        Tuple[str, float]: A tuple where the first element is k
                           and the second element is the square of v.
                           The type hint for the second element is float.
    """
    squared_v = v * v
    return (k, squared_v)
