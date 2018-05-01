
from flask.ext.restful import reqparse, Resource



parser = reqparse.RequestParser()
parser.add_argument('test', type=str)
parser.add_argument('txt', type=str)
class Home(Resource):
    def get(self):
        return {'hello': 'home'}

    def post(self):
        args = parser.parse_args()
        return args, 201