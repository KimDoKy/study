from multiprocessing import Process
import os

def f(x):
    print("{0} - 프로세스 ID: {1} (부모 프로세스 ID: {2})".format(x, os.getpid(), os.getppid()))

def main():
    for i in range(3):
        p = Process(target=f, args=(i, ))
        p.start()
    p.join()

if __name__ == "__main__":
    main()
