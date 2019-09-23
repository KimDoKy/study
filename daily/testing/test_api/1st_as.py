import requests
import random
import time
import asyncio

url = "http://localhost:8000/post/"
data = {'data':'sdfsf'}

def request_post():
    headers = {'Content-Type':'application/json; charset=utf-8'}
    for i in range(1000):
        res = requests.post(url, headers=headers, data=data)
    return res

@asyncio.coroutine
def generate():
    for i in range(5):
        asyncio.ensure_future(request_post())
    yield from asyncio.sleep(5)
 
def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(generate())
    loop.close()

try:
    t1 = time.time()
    main()
except:
    print('ex')
    main()
finally:
    t2 = time.time()
    print(t2-t1)
