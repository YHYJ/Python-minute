#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""Socket_client_2"""


import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('', 6799))

# print(client_socket.recv(1024).decode('utf-8'))

while True:
    data = input('请输入：')
    if data == 'q' or data == 'Q':
        break
    else:
        client_socket.send(data.encode('utf-8'))
        print('服务器返回信息：%s\n' % client_socket.recv(1024).decode('utf-8'))
client_socket.send('q'.encode('utf-8'))
client_socket.close()
