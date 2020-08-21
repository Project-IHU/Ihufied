from flask import render_template
from flask_login import login_required
from . import portal

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
    return render_template('/portal/registered_students.html')

@portal.route('/modify_dept')
@login_required
def modify_dept():
    return render_template('/portal/modify_dept.html')