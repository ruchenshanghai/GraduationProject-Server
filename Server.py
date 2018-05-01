# coding=utf-8
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/zhihu/word', methods=['POST'])
def zhihu_word():
    return 'zhihu word'


if __name__ == '__main__':
    app.run(port=8081)
