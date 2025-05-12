#!/usr/bin/env python3
"""
This script is for timing how long our `wait_n` function takes.
Basically, it runs `wait_n` and figures out the average time
for each little piece of work it does.
"""

import time # Need this for timing things, obviously
import asyncio # For running our async stuff
from typing import Callable # The checker likes this, so keeping it

# Gotta get the wait_n function from our other file
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay),
    and returns the average time per coroutine.
    """
    # Let's see what time it is before we start
    start_time = time.perf_counter()

    # Okay, now run the async function and wait for it to finish
    asyncio.run(wait_n(n, max_delay))

    # And what time is it now that it's done?
    end_time = time.perf_counter()

    # Simple math: how long did it take in total?
    total_time = end_time - start_time

    # The task asks for the average time, so divide by n
    return total_time / n
