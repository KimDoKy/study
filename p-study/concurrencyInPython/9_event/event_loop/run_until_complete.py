# 자체적으로 종료하기 전에 이벤트 루프가 주어진다.
import asyncio
import time

async def myWork():
    print("Starting Work")
    time.sleep(5)
    print("Ending Work")

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(myWork())
    loop.stop() # 이벤트 루프를 적절한 지점에서 멈추게 한다.
    print('Loop Stopped')
    loop.close()

    print(loop.is_closed())

if __name__ == "__main__":
    main()
