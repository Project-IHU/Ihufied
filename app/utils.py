import secrets
import random
import os
from PIL import Image
import base64
from resizeimage import resizeimage
from ihufied import app


def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
	
	i = Image.open(form_picture)
	i = resizeimage.resize_cover(i, [300, 250], validate=False)
	i.save(picture_path)
	
	with open(picture_path, "rb") as imageFile:
		encoded_string = base64.b64encode(imageFile.read())

	return [picture_fn, encoded_string]

def delete_picture(pic_name):
	picture_path = os.path.join(app.root_path, 'static/images', pic_name)
	os.remove(picture_path)
