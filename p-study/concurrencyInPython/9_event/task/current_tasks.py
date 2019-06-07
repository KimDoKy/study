# 모든 코루틴이 정상적으로 실행하고,
# 실행 중인 코루틴은 메인 코루틴이 실행될 때까지 보류
import asyncio

async def myCoroutine():
    print('My Coroutine')

async def main():
    current = asyncio.Task.current_task()
    print(current)

loop = asyncio.get_event_loop()
try:
    loop.create_task(myCoroutine())
    loop.create_task(myCoroutine())
    loop.create_task(myCoroutine())
    loop.run_until_complete(main())
finally:
    loop.close()



