from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required
from ihufied import db
from . import portal
from app.models import User, Faculty, Department, Course
from app.portal.forms import MakeFacultyForm, MakeDepartmentForm, MakeCourseForm

###################
#### ALL-VIEWS ####
###################

@portal.route('/register_student')
@login_required
def register_student():
    return render_template('/portal/register_student.html')

@portal.route('/remote_monitoring')
@login_required
def remote_monitoring():
    return render_template('/portal/monitoring.html')

@portal.route('/registered_students')
@login_required
def registered_students():
	page = request.args.get('page', 1 , type=int)
	students = User.query.order_by(User.lastname.asc()).paginate(page=page, per_page=25)
	return render_template('/portal/registered_students.html', students=students)

@portal.route('/modify_dept')
@login_required
def modify_dept():
	makefacultyform = MakeFacultyForm()
	makedepartmentform = MakeDepartmentForm()
	makecourseform = MakeCourseForm()
	return render_template('/portal/modify_dept.html',makefacultyform=makefacultyform,makedepartmentform=makedepartmentform,makecourseform=makecourseform)

@portal.route('/create_faculty', methods=['POST'])
@login_required
def create_faculty():
	form = MakeFacultyForm()
	try:
		if form.validate_on_submit():
			faculty = Faculty(name=form.name.data)
			db.session.add(faculty)
			db.session.commit()
			flash('Faculty created!', 'success')
			return redirect(url_for('portal.modify_dept'))
		else:
			flash('Please fill in the form correctly!', 'warning')
			return redirect(url_for('portal.modify_dept'))
	except Exception as e:
		flash('{}'.format(e), 'warning')
		return redirect(url_for('portal.modify_dept'))

@portal.route('/create_department', methods=['POST'])
@login_required
def create_department():
	form = MakeDepartmentForm()
	try:
		if form.validate_on_submit():
			department = Department(name=form.name.data,faculty_id=str(form.faculty.data))
			db.session.add(department)
			db.session.commit()
			flash('Department created!', 'success')
			return redirect(url_for('portal.modify_dept'))
		else:
			flash('Please fill in the form correctly!', 'warning')
			return redirect(url_for('portal.modify_dept'))
	except Exception as e:
		flash('{}'.format(e), 'warning')
		return redirect(url_for('portal.modify_dept'))

@portal.route('/create_course', methods=['POST'])
@login_required
def create_course():
	form = MakeCourseForm()
	try:
		if form.validate_on_submit():
			course = Course(name=form.name.data,department_id=str(form.department.data),title=form.title.data)
			db.session.add(course)
			db.session.commit()
			flash('Course created successfully.', 'success')
			return redirect(url_for('portal.modify_dept'))
		else:
			flash('Please fill in the form correctly!', 'warning')
			return redirect(url_for('portal.modify_dept'))
	except Exception as e:
		flash('{}'.format(e), 'warning')
		return redirect(url_for('portal.modify_dept'))