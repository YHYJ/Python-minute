import socket
# Host: sdual.boxuegu.com
# Connection: keep-alive
# Cache-Control: max-age=0
# Upgrade-Insecure-Requests: 1
# Save-Data: on
# User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.8
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'sdual.boxuegu.com'
    host = 'www.baidu.com'
    sock.connect((host,80))

    msg = '''GET / HTTP/1.1
Host: www.baidu.com
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Save-Data: on\r\n\r\n'''
    sock.send(msg.encode())
    while True:
        print(sock.recv(4096).decode())

main()