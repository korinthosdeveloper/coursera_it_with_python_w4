#!/usr/bin/env python3

import requests
import os

#where to upload photos
url = "http://localhost/upload/"
#get user variable and make the files path
user = os.getenv("USER")
path = "/home/{}/images/modified_jpg/".format(user)

files = os.listdir(path)

for file in files:
	if os.path.isfile(path+file):

		name, ext = os.path.splitext(file)
		if ext == ".jpg":
			with open(path+name+ext, "rb") as file_binary:
				print("The: {} is {} \n".format(file, file_binary))
				#r = requests.post(url, files={"file": file_binary})

