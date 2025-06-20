#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    host = request.headers.get('Host')
    return f'<h1>The host for this page is {Host}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
