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
        yield random.uniform(0, 10)
        i += 1
