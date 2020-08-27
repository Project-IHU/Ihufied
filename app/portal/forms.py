from flask_wtf import FlaskForm
from app.models import User, Department, Faculty
from wtforms import StringField, TextAreaField, SelectField, IntegerField, DateField, PasswordField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField

def department_query():
	return Department.query

def faculty_query():
	return Faculty.query

class MakeStudentForm(FlaskForm):
	firstname = StringField('',
		validators=[DataRequired('Please fill in your firstname')])
	lastname = StringField('',
		validators=[DataRequired('Please fill in your lastname')])
	middlename = StringField('')
	department = QuerySelectField(query_factory=department_query, allow_blank=True, get_label='name')
	regnumber = StringField('', validators=[DataRequired('Please fill in registration number')])
	level = SelectField('', choices=[('',''),('100','100'),('200','200'),('300','300'),('400','400'),('500','500')])
	email = StringField('', validators=[DataRequired('Please fill in a valid Email')])
	phone = IntegerField('', validators=[DataRequired('Please fill in your phone number')])
	image = FileField('', validators=[FileAllowed(['jpg','png', 'jpeg','JPG','JPEG','PNG'])])

	def __init__(self, *args, **kwargs):
		kwargs['csrf_enabled'] = False
		super(MakeStudentForm, self).__init__(*args, **kwargs)

	def validate_regnumber(self, regnumber):
		user = User.query.filter_by(regnumber=regnumber.data).first()
		if user:
			raise ValidationError('Reg number already exists!')


class RegisterStudentCourse(FlaskForm):
	regnumber = IntegerField('',
		validators=[DataRequired('Please fill in a reg number')])

	def __init__(self, *args, **kwargs):
		kwargs['csrf_enabled'] = False
		super(RegisterStudentCourse, self).__init__(*args, **kwargs)

class MakeFacultyForm(FlaskForm):
	name = StringField('',
		validators=[DataRequired('Please fill in the faculty name')])

	def __init__(self, *args, **kwargs):
		kwargs['csrf_enabled'] = False
		super(MakeFacultyForm, self).__init__(*args, **kwargs)

class MakeDepartmentForm(FlaskForm):
	name = StringField('',
		validators=[DataRequired('Please fill in the faculty name')])
	faculty = QuerySelectField(query_factory=faculty_query, allow_blank=True, get_label='name', validators=[DataRequired('Please select a faculty')])

	def __init__(self, *args, **kwargs):
		kwargs['csrf_enabled'] = False
		super(MakeDepartmentForm, self).__init__(*args, **kwargs)