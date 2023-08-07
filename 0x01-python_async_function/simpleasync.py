import asyncio
import time


async def do_this():
    print('Doing this, wait please')
    await asyncio.sleep(1)
    print('Done this!')


async def do_somethingelse():
    print('Doing something else')


async def main():
    await asyncio.gather(do_this(), do_somethingelse())


asyncio.run(main())
# print('Doing something else while do_this running!')


async def while_waiting():
    print('This is me waiting for do_that')


async def do_that():
    print('Doing that')
    await while_waiting()
    print('Done that')

# asyncio.run(do_that())
