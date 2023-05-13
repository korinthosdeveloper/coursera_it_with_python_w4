#!/usr/bin/env python3

#program to convert images to jpg and low resolution
import os
from PIL import Image

#where images directory are
user  = os.getenv("USER")
images_path = "/home/{}/supplier-data/images/".format(user)

#put files in a list
images_dir = os.listdir(images_path)

#the desired size
size = 600, 400

#for every file in list
#check if is file first
for im_file in images_dir:
	if os.path.isfile(images_path+im_file):
		#split text function to get the file name and its extension
		file, ext = os.path.splitext(im_file)
		#open file as image obj only if is a .tiff file
		if ext == ".tiff":
			with Image.open(images_path+file+ext) as im:
				#save the new file
				im.convert("RGB").resize(size).save(images_path+file+".jpeg", "JPEG")

