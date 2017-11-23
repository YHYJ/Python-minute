import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(("127.0.0.1",8080))
sock.listen(1)
sock1,addr=sock.accept()

print(sock1.recv(4096).decode())