import asyncio

async def print_after(message, delay):
    await asyncio.sleep(delay)
    print(message)


async def main():
    first_awaitable = print_after('world', 2)
    second_awaitable = print_after('hello', 1)
    await first_awaitable
    await second_awaitable

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
