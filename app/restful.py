from flask_restful import Resource, Api
from models import *

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')

api = Api(app)

class GetUser(Resource):
	def get(self):
		users = User.query.all()
		return users


api.add_resource(GetUser, '/getuser')