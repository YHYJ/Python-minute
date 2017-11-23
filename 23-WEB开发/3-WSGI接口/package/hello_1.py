#!/home/yj/.virtualenvs/py3.6.2/bin/python
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-09-11 20:02:54
Last modified: 2017-09-11 20:02:54
Python release: 3.6.2

web应用程序的WSGI处理函数
"""


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html'), ])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

