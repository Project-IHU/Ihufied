from datetime import datetime
from flask import render_template
from flask_login import login_required
from . import main
# from flask_restful import Resource, Api
from app.models import User, Faculty, Department, Course
import json

#api = Api(main)

###################
#### ALL-VIEWS ####
###################

@main.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())


@main.route('/getuser/<string:course_title>')
def getuser(course_title):
	try:
		course_title= course_title.upper()
		course = Course.query.filter_by(title=course_title).first()
		users = course.course_subscribers
		students_list = []
		for student in users:
			students = {}
			students['firstname'] = student.firstname
			students['lastname'] = student.lastname
			students['regnumber'] = student.regnumber
			students['image'] = str(student.image)
			students_list.append(students)
		if students_list == []:
			return 'No student registered!'
		else:
			return json.dumps(students_list)
	except AttributeError:
		return 'Course not found!'

#getting only students in that department registered can be done by inserting the id into the routing channel
	

# class GetUser(Resource):

# 	def get(self):
# 		users = User.query.all()
# 		return users


# api.add_resource(GetUser, '/getuser')
