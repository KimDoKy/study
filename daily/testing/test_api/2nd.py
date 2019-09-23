import multiprocessing
from executor.requestSecond import RequestPost
import time
import queue

procs = []

if __name__ == "__main__":
    m = multiprocessing.Manager()
    pipe_list = []
    sharedQueue = m.Queue()
    a = RequestPost('http://localhost:8000/test2/')
    t1 = time.time()
    for i in range(4):
        recv_end, send_end = multiprocessing.Pipe(False)
        proc = multiprocessing.Process(target=a.run, args=(i, send_end))
        procs.append(proc)
        pipe_list.append(recv_end)
        proc.start()
    for proc in procs:
        proc.join()
    t2 = time.time()
    print(t2-t1)
    print(pipe_list)
#results = [x.recv() for x in pipe_list]
#   print('total count: ', sum(results))

