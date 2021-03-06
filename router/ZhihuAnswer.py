from flask_restful import reqparse, Resource
from controller.ExtractTopic import extract_topic

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

parser = reqparse.RequestParser()

parser.add_argument('txt', type=str)
parser.add_argument('keyword_count', type=int)


class ZhihuAnswer(Resource):
    def get(self):
        return {'hello': 'zhihu answer'}

    def post(self):
        args = parser.parse_args()
        _parsed_count = args['keyword_count']
        if args['txt']:
            _parsed_txt = args['txt']
            _res_result = extract_topic(_parsed_txt, _parsed_count)
            return _res_result
        else:
            return {'status': False}, 200
        # return args['txt'], 200
