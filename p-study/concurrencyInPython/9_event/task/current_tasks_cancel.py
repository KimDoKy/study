# cancel(): 퓨처나 코루틴을 취소
import asyncio

async def myCoroutine():
    print('My Coroutine')

async def main():
    current = asyncio.Task.current_task()
    print(current)

loop = asyncio.get_event_loop()
try:
    task1 = loop.create_task(myCoroutine()) # task1,2 는 정상 작동
    task2 = loop.create_task(myCoroutine())
    task3 = loop.create_task(myCoroutine())
    task3.cancel()                          # 취소 호출로 실행 안됨
    loop.run_until_complete(main())
finally:
    loop.close()



