import time
import asyncio
import aiohttp
from bs4 import BeautifulSoup as bs

async def get_text_from_url(url):
    print(f'Send request to ...{url}')
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url, headers={'user-agent':'Mozilla/5.0'}) as res:
            text = await res.text()

    print(f'Get response from ...{url}')
    text = bs(text, 'html.parser').text
    print(text[:100].strip())

async def main():
    base_url = 'https://www.macmillandictionary.com/us/dictionary/american/{keyword}'
    keywords = ['hi', 'apple', 'call', 'feel', 'hello', 'bye', 'like', 'love']
    futures = [asyncio.ensure_future(get_text_from_url(
                base_url.format(keyword=keyword))) for keyword in keywords]
    await asyncio.gather(*futures)

if __name__ == "__main__":
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    end = time.time()
    print(f'time take: {end-start}')

