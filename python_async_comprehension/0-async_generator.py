#!/usr/bin/env python3
"""
This module contains an asynchronous generator.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    An asynchronous generator coroutine that yields random numbers.

    The coroutine loops 10 times, each time asynchronously waiting
    1 second, then yielding a random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
