from requests import get

'''
This is a code that can be implemented in the raspberry pi. The course title can be changed to any of the
courses that have been registered on the site. better still, user can be requested to insert input of the course.
'''

course_title = 'MEC501'
url = 'http://127.0.0.1:5000/{}'.format(course_title)

get(url).json()