## Python Aysnc Function

### Learning Objectives:

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

### Resources:

- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [asyncio.gather](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather)
- [asyncio.create_task](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task)
- [asyncio.sleep](https://docs.python.org/3/library/asyncio-task.html#asyncio.sleep)

### Tasks:

- Write a coroutine called wait_random that takes in an integer max_delay and waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.
- Write a coroutine called wait_n that takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay.
- Write a coroutine called wait_random that takes in an integer max_delay and waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.
- Write a coroutine called wait_n that takes in 2 int arguments (in this order): n and max_delay. You will spawn wait_random n times with the specified max_delay.
- Import wait_n from 1-async_comprehension.py.
- Write a coroutine called async_generator that takes no arguments. The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.
