from multiprocessing import Process, Lock

def f(lock, i):
    lock.acquire()

    print('{0}번째 프로세스 실행 중'.format(i))

    lock.release()

def main():
    lock = Lock()

    for i in range(3):
        p = Process(target=f, args=(lock, i))
        p.start()
    p.join()

if __name__ == "__main__":
    main()
