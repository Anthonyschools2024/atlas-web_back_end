#!/usr/bin/env python3
"""
Module for executing multiple asynchronous coroutines concurrently.

This module defines the `wait_n` coroutine, which spawns another
coroutine, `wait_random`, multiple times and collects the results
in ascending order of completion.
"""

import asyncio
from typing import List

# Import the wait_random coroutine from the previous task's file.
# The __import__ function is used as per the project's main file examples.
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawns `wait_random` `n` times with `max_delay`.

    This coroutine launches `n` instances of `wait_random(max_delay)`
    concurrently. It then gathers the float delay values returned by each
    `wait_random` call. The list of these delays is returned in ascending
    order. This order is achieved naturally by processing the tasks as
    they complete, leveraging `asyncio.as_completed`, without needing
    an explicit sort.

    Args:
        n: The number of times `wait_random` should be spawned.
           This must be an integer.
        max_delay: The maximum delay (in seconds) that will be passed
                   to each `wait_random` call. This must be an integer.

    Returns:
        A list of floats, where each float is a delay returned by
        a `wait_random` call. The list is sorted in ascending order
        based on the completion time of the coroutines.
    """
    # Create a list of tasks to be run.
    # Each task is a call to wait_random(max_delay) wrapped by asyncio.create_task
    # to schedule it for concurrent execution.
    tasks_to_run = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # Initialize an empty list to store the delays as they are completed.
    # This line was the source of previous SyntaxErrors and is now corrected.
    list_of_delays: List[float] =

    # Use asyncio.as_completed to iterate over the tasks as they finish.
    # This ensures that we process results in the order of their completion,
    # which naturally gives us the delays in ascending order.
    for completed_task_future in asyncio.as_completed(tasks_to_run):
        # Await the result (the delay) from the task that just completed.
        delay_value = await completed_task_future
        list_of_delays.append(delay_value)

    return list_of_delays
