
#!/usr/bin/env python3
"""
Module demonstrating concurrent execution of asynchronous coroutines.

This script defines `wait_n`, an asynchronous function that manages
multiple calls to another coroutine, `wait_random`, and collects
their results based on completion order.
"""

import asyncio
from typing import List

# Import the base coroutine from the specified module
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `wait_random` multiple times and gathers the resulting delays.

    This coroutine will initiate `n` concurrent calls to `wait_random`,
    each configured with the `max_delay`. It then collects the float
    delay values returned by each call. The final list of delays
    is presented in ascending order, naturally achieved by processing
    coroutines as they complete.

    Parameters:
        n (int): The quantity of `wait_random` coroutines to launch.
        max_delay (int): The upper limit for the random delay in each
                         `wait_random` call.

    Returns:
        List[float]: A list containing the float delay values, sorted
                     implicitly by the order of coroutine completion.
    """
    # Prepare a list of all tasks to be executed.
    # Each task is an instance of wait_random(max_delay) scheduled for execution.
    task_list = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # This list will store the delays as they are returned by completed tasks.
    results_list =

    # asyncio.as_completed() provides an iterator that yields tasks as they finish.
    # This allows processing results in the order of completion.
    for finished_task_future in asyncio.as_completed(task_list):
        # Retrieve the actual delay value from the completed task.
        current_delay = await finished_task_future
        results_list.append(current_delay)

    # Return the list of delays, which will be in ascending order.
    return results_list
