from multiprocessing import Process, Pipe
import os

def sender(conn):
    conn.send('Hello World')
    conn.close()

def receiver(conn):
    msg = conn.recv()
    print('메시지 수신: {0}'.format(msg))
    conn.close()

def main():
    parent_conn, child_conn = Pipe()
    p = Process(target=sender, args=(child_conn,))
    p.start()

    p = Process(target=receiver, args=(parent_conn, ))
    p.start()

    p.join()

if __name__ == "__main__":
    main()
