# run_forever() : 이벤트 루프를 시작해 계속 블로킹
# n개의 코루틴에서 계속 동작하는 이벤트 루프를 생성

import asyncio

@asyncio.coroutine
def hello_world():
    yield from asyncio.sleep(1)
    print('Hello world')
    asyncio.async(hello_world())

@asyncio.coroutine
def good_evening():
    yield from asyncio.sleep(1)
    print('Good Evening')
    asyncio.async(good_evening())

print('step: asyncio.get_event_loop()')
loop = asyncio.get_event_loop()
try:
    print('step: loop.run_until_complete()')
    asyncio.async(hello_world())
    asyncio.async(good_evening())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print('step: loop.close()')
    loop.close()
