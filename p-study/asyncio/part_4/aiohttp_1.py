import aiohttp
import asyncio

async def fetch_and_print(url):
    async with aiohttp.ClientSession() as session:
        res = await session.get(url)
        print(await res.text())

loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_and_print('https://python.org/'))
