from requests import get
import base64

'''
This is a code that can be implemented in the raspberry pi. The course title can be changed to any of the
courses that have been registered on the site. better still, user can be requested to insert input of the course.
'''
def decode_images(students):
	for student in students:
		'''
			the next three lines converts/encodes the string formatted image back to base64, which is then decoded
			to raw image format and stored in the folder "registered_student_img" using the reg number of the 
			student.
		'''
		image_encode = student['img'].encode('utf-8')
		image_decode = base64.decodebytes(image_encode)
		image_result = open('registered_student_img/{}.png'.format(student['reg_no']), 'wb')
		image_result.write(image_decode)

course_title = 'MEC501'
url = 'http://127.0.0.1:5000/getuser/{}'.format(course_title)

students = get(url).json()

decode_images(students)

