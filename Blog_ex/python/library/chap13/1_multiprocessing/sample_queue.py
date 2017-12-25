from multiprocessing import Process, Queue

def sender(q, n):
    q.put('{0}회째의 Hello World'.format(n))

def main():
    q = Queue()
    for i in range(3):
        p = Process(target=sender, args=(q, i))
        p.start()

    print(q.get())
    print(q.get())

    p.join()

if __name__ == "__main__":
    main()
