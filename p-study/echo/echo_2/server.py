import socketserver

HOST = ''
PORT = 9009
# 클라이언트의 요청에 대한 처리를 담당
# TCPServer가 객체화 될때 단 한번 초기화 됨
class MyTcpHandler(socketserver.BaseRequestHandler):
    # 클라이언트의 연결과 요청 작업을 처리
    # client_address는 BaseRequestHandler의 클래스 맴버
    # client_address는 클라이언트의 IP 주소를 담고 있음
    def handle(self):
        print(f'connect [{self.client_address[0]}]')

        try:
            while True:
                # request는 BaseRequestHandler의 클래스 맴버
                # request는 클라이언트 소켓과 연견된 서버의 TCP 소켓
                self.data = self.request.recv(1024)
                if self.data.decode() == '/quit':
                    print(f'[{self.client_address[0]}]에 의해 중단')
                    return

                print(f'[{self.data.decode()}]')
                self.request.sendall(self.data)
        except Exception as e:
            print(e)

def runServer():
    print('+++ start Echo Server')
    print('Press the Ctrl+C button to exit the echo server')
    
    try:
        server = socketserver.TCPServer((HOST, PORT), MyTcpHandler)
        # ctrl+c 혹은 server.shutdown() 호출이 있기 전까지 클라이언트 대기
        server.serve_forever()
    except KeyboardInterrupt:
        print('--- close Echo Server')

runServer()
