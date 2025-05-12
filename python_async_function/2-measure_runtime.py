#!/usr/bin/env python3
"""
Module to measure the runtime of an asynchronous operation.

This module provides a function `measure_time` that calculates
the average execution time per operation for the `wait_n` coroutine.
"""

import asyncio
import time

# Import wait_n from the previous file (1-concurrent_coroutines.py)
# using the __import__ method as demonstrated in the project's main files.
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per spawned operation (total_time / n).

    This function is synchronous but calls an asynchronous function
    internally. It uses `time.perf_counter()` for accurate time
    measurement and `asyncio.run()` to execute the `wait_n` coroutine.

    Args:
        n: The number of times `wait_n` will spawn `wait_random`.
           This is an integer.
        max_delay: The maximum delay (in seconds) to be passed to each
                   `wait_random` call within `wait_n`. This is an integer.

    Returns:
        A float representing the average execution time per `wait_random`
        call that was spawned by `wait_n`. This is calculated as
        the total execution time of `wait_n` divided by `n`.
    """
    # Record the start time before executing the asynchronous operation.
    # time.perf_counter() provides a high-resolution clock for measuring
    # short durations.
    start_timestamp: float = time.perf_counter()

    # Execute the asynchronous wait_n function.
    # asyncio.run() is the standard way to run an asyncio program's
    # entry point coroutine from synchronous code.
    asyncio.run(wait_n(n, max_delay))

    # Record the end time after the asynchronous operation has completed.
    end_timestamp: float = time.perf_counter()

    # Calculate the total elapsed time for the execution of wait_n.
    total_execution_time: float = end_timestamp - start_timestamp

    # Calculate and return the average time per operation.
    average_time_per_operation: float = total_execution_time / n

    return average_time_per_operation
