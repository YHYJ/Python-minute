#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

class Hello():

    def __init__(self, name='world'):
        self.name = name

    def hello(self):
        print("Hello,%s" % self.name)

if __name__ == '__main__':
    h = Hello(name='YJ')
    h.hello()
