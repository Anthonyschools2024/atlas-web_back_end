#!/usr/bin/env python3
"""
Module for executing multiple coroutines concurrently.

This module provides an asynchronous routine `wait_n` that
spawns multiple instances of the `wait_random` coroutine
and collects their results in ascending order of completion time.
"""

import asyncio
from typing import List

# Import wait_random from the previous file (0-basic_async_syntax.py)
# as demonstrated in the provided main files.
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns wait_random n times with a specified max_delay.

    This coroutine creates `n` tasks, each running `wait_random(max_delay)`.
    It then waits for these tasks to complete and collects the delay
    returned by each. The list of delays is returned in ascending order,
    which is achieved by processing tasks as they complete, rather than
    explicitly sorting the final list.

    Args:
        n: The number of times to call/spawn wait_random.
           Must be a non-negative integer.
        max_delay: The maximum delay (in seconds) to be passed to each
                   wait_random call. Must be a non-negative integer.

    Returns:
        A list of float values. Each float is a delay returned by
        a `wait_random` call. The list is sorted in ascending order
        based on the completion time of the coroutines.
    """
    if n <= 0:
        return  # Corrected: Return an empty list for n <= 0

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    completed_delays: List[float] =  # Corrected: Initialize as an empty list
    for task_future in asyncio.as_completed(tasks):
        delay = await task_future
        completed_delays.append(delay)

    return completed_delays
