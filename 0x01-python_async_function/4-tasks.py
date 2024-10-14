#!/usr/bin/env python3

import asyncio
from typing import List

"""
Take the code from wait_n and alter it into a new function task_wait_n
"""

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Take the code from wait_n and alter it into a new function
    task_wait_n. The code is nearly identical to wait_n except
    task_wait_random is being called
    """

    delays: List[float] = []
    orderList: List[float] = []

    for k in range(n):
        delays.append(task_wait_random(max_delay))

    for l in asyncio.as_completed(delays):
        orderList.append(await l)

    return orderList
