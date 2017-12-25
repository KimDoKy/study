from multiprocessing import Process

def f(i):
    print('{0}번째 프로세스 실행 중'.format(i))

def main():
    for i in range(3):
        p = Process(target=f, args=(i, ))
        p.start()
    p.join()

if __name__ == "__main__":
    main()
