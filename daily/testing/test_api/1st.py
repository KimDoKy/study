import requests
import random
import time
from multiprocessing import Process

url = "http://localhost:8000/post/"
data = {'data':'sdfsf'}

def request_post():
    headers = {'Content-Type':'application/json; charset=utf-8'}
    for i in range(1000):
        res = requests.post(url, headers=headers, data=data)

procs = []


t1 = time.time()

def main():
    for i in range(10):
        proc = Process(target=request_post, args=())
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()

try:
    main()
except:
    print('except')
    main()
finally:
    t2 = time.time()
    print(t2-t1)
