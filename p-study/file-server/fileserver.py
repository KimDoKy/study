import socketserver
from os.path import exists

HOST = ''
PORT = 9009
class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data_transferred = 0
        print(f'connect [{self.client_address[0]}]')
        filename = self.request.recv(1024)
        filename = filename.decode()

        if not exists(filename):
            return

        print(f'파일 [{filename}] 전송 시작.')
        with open(filename, 'rb') as f:
            try:
                data = f.read(1024)
                while data:
                  data_transferred += self.request.send(data)
                  data = f.read(1024)
            except Exception as e:
                print(e)

        print(f'전송완료 [{filename}], 전송량[{data_transferred}]')

def runServer():
    print('+++ start File Server')
    print('Press the Ctrl+C button to exit the File server')
    
    try:
        server = socketserver.TCPServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('--- close File Server')

runServer()
