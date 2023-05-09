#!/usr/bin/env python3

#script to upload description and image to server
import os
import requests
import re


#url to upload fruit descriptions
url = "http://[linux-insta-ip]/fruits"
#get env variable of user 
user = os.getenv("USER")
#find path of files
path = ("/home/{}/supplier-data/description/".format(user))
#find dir of files
textDir = os.listdir(path)

data = {}
#process the files to create the data dir
for file in textDir:
	#take the file name to use for image file
	name, ext = os.path.splitext(file)
	with open(path+file, "r") as openedFile:
		#read all file lines
		lines = openedFile.readlines()
		#remove '\n' char
		data["name"] = lines[0].strip("\n ")
		# get weight with regex & convert it to int
		data["weight"] = int(re.search("[0-9]*", lines[1].strip("\n "))[0])
		data["description"] = lines[2].strip("\n ")
		data["image_name"] = name+".jpg"
		#we want to upload json object to django server
		r = requests.post(url, json= data)


