#!/usr/bin/env python3
"""
Module for basic asynchronous syntax.

This module contains an asynchronous coroutine `wait_random`
that demonstrates waiting for a random amount of time using asyncio.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay and returns the delay.

    This coroutine takes an integer argument `max_delay`, which defaults
    to 10. It then generates a random floating-point number between 0
    and `max_delay` (inclusive). The coroutine will pause execution
    for this random duration before eventually returning the duration
    it waited.

    Args:
        max_delay: An integer representing the maximum possible delay
                   in seconds. The actual delay will be a float
                   between 0 and this value. Defaults to 10.

    Returns:
        A float representing the actual number of seconds waited.
    """
    actual_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(actual_delay)
    return actual_delay
