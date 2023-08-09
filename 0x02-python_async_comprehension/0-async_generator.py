#!/usr/bin/env python3
"""async_generator module """

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """async_generator function """
    i = 0
    while i < 10:
        await asyncio.sleep(1)
        yield random.random() * 10
        i += 1


async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
