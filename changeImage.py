#!/usr/bin/env python3

#program to convert images to jpg and low resolution
import os
from PIL import Image

#where images directory are
user  = os.getenv("USER")

images_path = "/home/{}/images/".format(user)
#here give the new path
new_path = "/home/{}/images/modified_jpg/".format(user)

#put files in a list
images_dir = os.listdir(images_path)

#the desired size
size = 600, 400

#for every file in list
#check if is file first
for im_file in images_dir:
	if os.path.isfile(images_path+im_file):
		#split ext
		file, ext = os.path.splitext(im_file)
		#open file as image obj
		with Image.open(images_path+file+ext) as im:
			#save the new file
			im.convert("RGB").resize(size).save(new_path+file+".jpg", "JPEG")

