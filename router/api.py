from flask import Flask
from flask.ext import restful
from flask_cors import CORS

from Home import Home
from ZhihuAnswer import ZhihuAnswer

app = Flask(__name__)
api = restful.Api(app)
CORS(app, resources=r'/*')


api.add_resource(Home, '/')
api.add_resource(ZhihuAnswer, '/zhihu-answer')

if __name__ == '__main__':
    app.run(port=8081, debug=True)