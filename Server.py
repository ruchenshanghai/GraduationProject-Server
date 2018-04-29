# coding=utf-8

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    test1 = 123
    test2 = 'test'
    print '%d %s' % (test1, test2)
    app.run()
