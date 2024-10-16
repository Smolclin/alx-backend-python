#!/usr/bin/env python3

"""
Import async_comprehension from the previous file and write a measure_runtime
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    should measure the total runtime and return it
    """

    time_started = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - time_started
