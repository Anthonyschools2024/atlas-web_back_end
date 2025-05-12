#!/usr/bin/env python3
"""
This module contains a coroutine that uses async comprehension.
"""

from typing import List

# Import async_generator using __import__ due to the leading digit in the module name
async_generator_module = __import__('0-async_generator')
async_generator = async_generator_module.async_generator
# Or, more directly, though slightly less readable for some:
# async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over async_generator.

    Returns:
        List[float]: A list containing 10 random floating-point numbers
                     yielded by async_generator.
    """
    numbers = [i async for i in async_generator()]
    return numbers
