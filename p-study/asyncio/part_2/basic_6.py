import asyncio
import sqlite3
import time

async def sleep():
    await asyncio.sleep(1)

async def main():
    futures = [
        asyncio.ensure_future(sleep()) for i in range(10000)
    ]
    await asyncio.gather(*futures)

if __name__ == '__main__':
    start = time.time()
    asyncio.ensure_future(main())
    end = time.time()
    print(f'{end-start}')
