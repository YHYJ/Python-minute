#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Socket_client_2"""


import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('', 6799))

# print(client_socket.recv(1024).decode('utf-8'))

while True:
    data = input('Please input: ')
    if data == 'q' or data == 'Q':
        break
    else:
        client_socket.send(data.encode('utf-8'))
        print('The server returned : %s\n' % client_socket.recv(1024).decode('utf-8'))
client_socket.send('q'.encode('utf-8'))
client_socket.close()
