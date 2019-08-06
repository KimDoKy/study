# all_tasks() : 주어진 이벤트 루프 세트를 반환
# 이벤트 루프를 전달하지 않으면, 현재 이벤트 루프의 모든 테스크를 출력
import asyncio

async def myCoroutine():
    print('My Coroutine')

async def main():
    await asyncio.sleep(1)

loop = asyncio.get_event_loop()
try:
    loop.create_task(myCoroutine())
    loop.create_task(myCoroutine())
    loop.create_task(myCoroutine())

    pending = asyncio.Task.all_tasks()
    print(pending)
    loop.run_until_complete(main())
finally:
    loop.close()
