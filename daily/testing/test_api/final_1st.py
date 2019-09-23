from multiprocessing import Process
from executor.requestFirst import RequestPost
import time

procs = []

if __name__ == "__main__":
    a = RequestPost('http://localhost:8000/post/')
    t1 = time.time()
    for i in range(3):
        proc = Process(target=a.run, args=())
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()
    t2 = time.time()
    print(t2-t1)

