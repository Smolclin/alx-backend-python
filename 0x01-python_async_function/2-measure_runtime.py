#!/usr/bin/env python3

import time
import asyncio

""" From the previous file, import wait_n into 2-measure_runtime.py """

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Return the measured time
    """

    time_start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapse = time.perf_counter() - time_start
    return elapse / n
