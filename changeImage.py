#!/usr/bin/env python3

#program to convert images to jpg and low resolution
import os

#where images directory are
images_path = "/home/fedoritas/images/"

#put files in a list
images_dir = os.listdir(images_path)

#for every file in list
#check if is file first
for im_file in images_dir:
	if os.path.isfile(images_path+im_file):
		print(im_file)

