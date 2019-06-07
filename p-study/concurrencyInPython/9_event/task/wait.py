# wait() : 모든 퓨처, 코루틴에 전달된 첫 번째 파라미터가 완료될 때까지 프로그램을 블로킹
import asyncio

async def myCoroutine(i):
    print(f'My Coroutine {i}')

loop = asyncio.get_event_loop()
try:
    tasks = []
    for i in range(4):
        tasks.append(myCoroutine(i))
    loop.run_until_complete(asyncio.wait(tasks))
finally:
    loop.close()
