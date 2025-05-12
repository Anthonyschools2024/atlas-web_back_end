#!/usr/bin/env python3
"""
This module contains a coroutine to measure the runtime
of executing async_comprehension four times in parallel.
"""

import asyncio
import time

# Import async_comprehension using __import__
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather
    and measures the total runtime.

    Returns:
        float: The total time taken to execute the four comprehensions
               in parallel.
    """
    start_time = time.perf_counter()

    # Create and run the four tasks in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    # Alternative using a list comprehension / generator expression:
    # tasks = [async_comprehension() for _ in range(4)]
    # await asyncio.gather(*tasks)

    end_time = time.perf_counter()
    total_runtime = end_time - start_time
    return total_runtime
