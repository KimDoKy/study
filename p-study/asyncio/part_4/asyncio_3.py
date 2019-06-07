import asyncio

async def print_after(message):
    print(f'start of example(): {message}')
    await asyncio.sleep(1)
    print(f'end of example(): {message}')

async def main():
    first_awaitable = print_after('first call')
    second_awaitable = print_after('second call')
    await first_awaitable
    await second_awaitable

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
