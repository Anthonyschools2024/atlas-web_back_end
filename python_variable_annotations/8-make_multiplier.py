#!/usr/bin/env python3
"""
This module contains a type-annotated function 'make_multiplier'
that demonstrates higher-order functions and closures.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    This function takes a float `multiplier` and returns a new function.
    The returned function itself takes a float argument and multiplies
    it by the captured `multiplier`.

    Args:
        multiplier (float): The float value to be used as the multiplier
                            in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a single float
                                  argument and returns a float (the product).
    """
    def inner_multiplier_function(value: float) -> float:
        """
        Multiplies an input float by the captured outer 'multiplier'.

        Args:
            value (float): The float number to be multiplied.

        Returns:
            float: The result of 'value' * 'multiplier'.
        """
        return value * multiplier

    return inner_multiplier_function
