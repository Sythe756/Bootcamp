import asyncio

async def print_hello_world():
    while True:
        print('Hello ...')
        await asyncio.sleep(5)
        print('... World!')

async def main():
    # Create a task that runs the print_hello_world function
    task = asyncio.create_task(print_hello_world())

    # Wait for the task to complete (which it won't, as it runs infinitely)
    await task

asyncio.run(main())
