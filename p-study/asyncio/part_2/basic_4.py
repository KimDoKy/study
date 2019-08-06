import asyncio
import time

async def coroutine_1():
    print('코루틴 1 시작')
    print('코루틴 1 중단... 5초간 기다린다.')
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, time.sleep, 5)
    print('코루틴 1 재개')

async def coroutine_2():
    print('코루틴 2 시작')
    print('코루틴 2 중단... 4초간 기다린다.')
    await loop.run_in_executor(None, time.sleep, 4)
    print('코루틴 2 재개')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    start = time.time()
    loop.run_until_complete(asyncio.gather(coroutine_1(), coroutine_2()))
    end = time.time()

    print(f'time taken: {end-start}')
