#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""Socket_server"""


import time
import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)	 # 立即收回端口
server_socket.bind(('', 6799))
server_socket.listen(5)

print('[info]:等待连接...')


def tcplink(cs_sock, client_addr):
    print('[info]:接收来自 %s:%s 的连接...' % client_addr)
    cs_sock.send('Welcome!'.encode('utf-8'))
    while True:
        data = cs_sock.recv(1024)
        if not data or data.decode('utf-8') == 'q' or data.decode('utf-8') == 'Q':
            cs_sock.close()    # 关闭与客户端的socket连接
            server_socket.close()   # 关闭服务端socket
            print('[info]:链接 %s:%s 已关闭...' % client_addr)
            break
        print('客户端信息：%s' % data.decode('utf-8'))
        cs_sock.send(data.decode('utf-8').encode('utf-8'))

while True:
    cs_socket, client_addr = server_socket.accept()
    t = threading.Thread(target=tcplink, args=(cs_socket, client_addr))
    t.setDaemon(True)
    t.start()
