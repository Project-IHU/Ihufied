import secrets
import random
import os
from PIL import Image
from app import create_app
import base64
from resizeimage import resizeimage

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')

def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(app.root_path, "static/images", picture_fn)
	
	i = Image.open(form_picture)
	i = resizeimage.resize_cover(i, [300, 250], validate=False)
	i.save(picture_path)
	
	with open(picture_path, "rb") as imageFile:
		encoded_string = base64.b64encode(imageFile.read())

	return [picture_fn, encoded_string]

def update_picture (form_picture):
    
    # random_hex holds the random hexademicals generated
    random_hex = secrets.token_hex(8)
    # os.path.splitext returns the filename and the extention if it a file
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, "static/images", picture_fn)

    # this is where we resize the pictures which gives us a new image i
    output_size = (400, 400)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    # then we save i to the picture_path above
    i.save(picture_path)

    return picture_fn


def delete_picture(pic_name):
	picture_path = os.path.join(app.root_path, 'static/images', pic_name)
	os.remove(picture_path)
