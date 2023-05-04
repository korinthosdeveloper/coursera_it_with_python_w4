#!/usr/bin/env python3

#script to upload description and image to server
import os
import requests
import re

#get env variable of user 
user = os.getenv("USER")
#find path of files
path = ("/home/{}/supplier_description/".format(user))
#find dir of files
textDir = os.listdir(path)

data = {}
#process the files to create the data dir
for file in textDir:
	with open(path+file, "r") as openedFile:
		#read all file lines
		lines = openedFile.readlines()
		#remove '\n' char
		data["name"] = lines[0].strip("\n ")
		# get weight with regex & convert it to int
		data["weight"] = int(re.search("[0-9]*", lines[1].strip("\n "))[0])
		data["description"] = lines[2].strip("\n ")
		print(data)


