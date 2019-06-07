# 스케쥴링되고 실행될 이벤트 루프에 필요한 5개의 코루팅을 생성할 함수 정의
# 코루틴의 스케줄링을 위해 ensure_future() 메소드를 사용
import asyncio
import time

@asyncio.coroutine
def myTask(n):
    time.sleep(1)
    print(f'Processing {n}')

@asyncio.coroutine
def myGenerator():
    for i in range(5):
        asyncio.ensure_future(myTask(i))
    print('Completed Tasks')
    yield from asyncio.sleep(2)

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(myGenerator())
    loop.close()

if __name__ == "__main__":
    main()

