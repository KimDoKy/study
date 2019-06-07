import asyncio

async def print_after(message, delay):
    await asyncio.sleep(delay)
    print(message)

async def main():
    await asyncio.gather(
            print_after('world', 2),
            print_after('hello', 1)
            )

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
