import asyncio
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

async def sleep(executor=None):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(executor, time.sleep, 1)

async def main():
    executor = ThreadPoolExecutor(max_workers=10000)

    futures = [
        asyncio.ensure_future(sleep(executor)) for i in range(10000)
    ]
    await asyncio.gather(*futures)


if __name__ == "__main__":
    start = time.time()
    asyncio.ensure_future(main())
    end = time.time()
    print(f'time taken: {end-start}')
