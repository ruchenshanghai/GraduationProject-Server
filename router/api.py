from flask import Flask
import flask_restful
from flask_cors import CORS

from Home import Home
from ZhihuAnswer import ZhihuAnswer
from ZhihuTopic import ZhihuTopic
from ZhihuUser import ZhihuUser

app = Flask(__name__)
api = flask_restful.Api(app)
CORS(app, resources=r'/*')


api.add_resource(Home, '/')
api.add_resource(ZhihuAnswer, '/zhihu-answer')
api.add_resource(ZhihuTopic, '/zhihu-topic')
api.add_resource(ZhihuUser, '/zhihu-user')

if __name__ == '__main__':
    app.run(port=8081, debug=True)