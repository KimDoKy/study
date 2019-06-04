import socket

HOST = 'localhost'
PORT = 9009

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    while True:
        msg = input('input message: ')
        if msg == '/quit':
            socket.sendall(msg.encode())
            break

        sock.sendall(msg.encode())
        data = sock.recv(1024)
        print(f'message to server [{data.decode()}]')

print('close clinet')
