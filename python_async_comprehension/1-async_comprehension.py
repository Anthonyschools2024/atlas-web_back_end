#!/usr/bin/env python3
"""
This module contains a coroutine that uses async comprehension.
"""

from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over async_generator.

    Returns:
        List[float]: A list containing 10 random floating-point numbers
                     yielded by async_generator.
    """
    numbers = [i async for i in async_generator()]
    return numbers
