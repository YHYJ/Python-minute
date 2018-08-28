# -*- coding: utf-8 -*-

"""Socket_server"""


import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)	 # 立即收回端口
server_socket.bind(('', 6799))
server_socket.listen(5)

print('[info]:Waiting for connection...')


def tcplink(cs_sock, client_addr):
    print('[info]:%s:%s connected' % client_addr)
    cs_sock.send('Welcome!'.encode('utf-8'))
    while True:
        data = cs_sock.recv(1024)
        if not data or data.decode('utf-8') == 'q' or data.decode('utf-8') == 'Q':
            cs_sock.close()
            # server_socket.close()
            print('[info]:Connection %s:%s is closed' % client_addr)
            break
        print('Client information: %s' % data.decode('utf-8'))
        cs_sock.send(data.decode('utf-8').encode('utf-8'))

while True:
    cs_socket, client_addr = server_socket.accept()
    t = threading.Thread(target=tcplink, args=(cs_socket, client_addr))
    t.setDaemon(True)
    t.start()
