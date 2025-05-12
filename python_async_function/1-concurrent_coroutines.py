#!/usr/bin/env python3
"""Concurrent coroutines - wait_n"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.
    Return the list of delays in ascending order (naturally, via concurrency).
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delays.append(delay)

    return delays
