## socket methods

(client) socket method | 구현 로직 | (server) socket method | 구현 로직
---|---|---|---
`socket.socket()` | 소켓 객체 생성 | `socket.socket()` | 소켓 객체 생성
 | | `socket.bind()` | 생성한 소켓을 서버 IP 및 포토와 바인드
 | | `socket.listen()` | 처리 가능한 연결수 설정
`socket.connect()`| 서버에 연결 | `socket.accept()` | 클라이언트 요청을 기다리고 연결 요청이 오면 수락
`socket.send()`|서버로 메시지 전송 | `socket.recv()` | 클라이언트 요청 메시지 수신
 | | | 수신 메시지에 대한 처리
`socket.recv()`| 서버로부터 데이터 수신 | `socket.send()` <br>또는 <br>`socket.sendall()` | 클라이언트로 응답 데이터 송신
`socket.close()` | 소켓 객체 제거 | `socket.close()` | 소켓 객체 제거

