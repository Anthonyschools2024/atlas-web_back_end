#!/usr/bin/env python3
"""
Utility for timing the `wait_n` asynchronous operation.

This module provides a function to measure how long `wait_n` takes
to run and then calculates an average time per concurrent operation
it performs.
"""

import time
import asyncio
from typing import Callable  # Retained as per your provided script

# Importing the wait_n coroutine from the previous task's file.
# This is the function whose performance we are measuring.
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Runs `wait_n` and computes the average execution time per internal task.

    This function will:
    1. Record the time before starting `wait_n`.
    2. Execute `wait_n(n, max_delay)` to completion.
    3. Record the time after `wait_n` finishes.
    4. Calculate the total duration and then the average per `n` operations.

    Args:
        n (int): The number of concurrent `wait_random` calls that
                 `wait_n` will initiate.
        max_delay (int): The `max_delay` argument to be passed through
                         to `wait_n`.

    Returns:
        float: The average time (total_duration / n) taken for each of
               the `n` concurrent operations within `wait_n`.
    """
    # Get the timestamp right before we start the async operations.
    s_time = time.perf_counter()

    # Run the main asynchronous function we're timing.
    # asyncio.run() handles the event loop for this call.
    asyncio.run(wait_n(n, max_delay))

    # Get the timestamp immediately after the async operations complete.
    e_time = time.perf_counter()

    # Calculate the total time elapsed.
    duration = e_time - s_time

    # Compute the average time per operation and return it.
    return duration / n
