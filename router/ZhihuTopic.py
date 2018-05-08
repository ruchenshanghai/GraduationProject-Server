from flask_restful import reqparse, Resource
from controller.ExtractTopic import get_topic_by_id
from controller.ExtractQuestion import search_question_by_keyword

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

parser = reqparse.RequestParser()

parser.add_argument('id', type=int)


class ZhihuTopic(Resource):
    def get(self):
        args = parser.parse_args()
        _parse_id = args['id']
        _parse_topic = get_topic_by_id(_parse_id)
        if _parse_topic:
            _question_list = search_question_by_keyword(_parse_topic['name'])
            _parse_topic['question_list'] = _question_list
        return _parse_topic