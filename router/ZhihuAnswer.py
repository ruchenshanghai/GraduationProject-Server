
from flask.ext.restful import reqparse, Resource
import jieba
import jieba.analyse

parser = reqparse.RequestParser()

parser.add_argument('txt', type=str)
parser.add_argument('keyword_count', type=int)
parser.add_argument('keyword_type', type=str)

class ZhihuAnswer(Resource):
    def get(self):
        return {'hello': 'zhihu answer'}

    def post(self):
        args = parser.parse_args()
        _parse_type = 'default'
        _parse_count = 10
        _parse_txt = None
        if args['keyword_type']:
            _parse_type = args['keyword_type']
        if args['keyword_count']:
            _parse_count = args['keyword_count']
        if args['txt']:
            _parse_txt = args['txt']
            if _parse_type == 'recount':
                jieba.analyse.set_idf_path("../resource/idf_recount.txt")
            elif _parse_type == 'single_plus':
                jieba.analyse.set_idf_path("../resource/idf_recount.txt")

        else:
            return {'status': False}, 200
        # return args['txt'], 200
