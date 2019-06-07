import asyncio

async def echo(string):
    process = await asyncio.create_subprocess_exec('echo', string)
    await process.wait()

loop = asyncio.get_event_loop()
loop.run_until_complete(echo('hello, world'))

