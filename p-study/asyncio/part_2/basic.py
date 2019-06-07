import asyncio
import time

async def sleep():
    await asyncio.sleep(5)

start = time.time()
loop = asyncio.get_event_loop()

loop.run_until_complete(sleep())
end = time.time()

print(str(end-start) + 's')
