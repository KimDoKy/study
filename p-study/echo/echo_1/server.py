import socket

HOST = ''
PORT = 9009

def runServer():
    # TCP 소켓을 생성하고 socket 객체를 리턴
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        # 서버가 한 번에 처리 가능한 연결 수
        sock.listen(1)
        print('Waiting for client connection..')
        # 연결 요청이 오면 
        # 클라이언트와 연결된 TCP 소켓
        # 클라이언트 주소를 리턴
        conn, addr = sock.accept()
        with conn:
            print(f'connect [{addr[0]}]')
            while True:
                # 클라이언트로부터 1024 bite를 수신
                # 1024 ~ 4096 사이의 값을 권장
                data = conn.recv(1024)
                if not data:
                    break
                print(f'send message [{data.decode()}]')
                # 클라이언트 소켓인 conn을 통해 data을 통해 모두 전송
                # 모두 전송하면 None을 리턴
                conn.sendall(data)

runServer()
