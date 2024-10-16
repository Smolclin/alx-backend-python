#!/usr/bin/env python3
"""
Write a coroutine called async_generator that takes no arguments
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    the function yields random no after every 10 sec
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
