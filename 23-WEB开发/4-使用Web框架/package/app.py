#!/home/yj/.virtualenvs/py3.6.2/bin/python
# -*- coding: utf-8 -*-


from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('signin', methods=['GET'])
def