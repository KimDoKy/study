# 코루틴 세트 및 퓨처를 인자로 취해 입력된 세트로부터 종합된 결과를 future 객체로 반환한다.
import asyncio

async def myCoroutine(i):
    print(f'My Coroutine {i}')

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(asyncio.gather(myCoroutine(1), myCoroutine(2)))
finally:
    loop.close()
