from flask_restful import reqparse, Resource
from controller.ExtractUser import parse_user_by_id

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

parser = reqparse.RequestParser()

parser.add_argument('id', type=str)


class ZhihuUser(Resource):
    def get(self):
        args = parser.parse_args()
        _parse_id = args['id']
        _parsed_user = parse_user_by_id(_parse_id)
        return _parsed_user