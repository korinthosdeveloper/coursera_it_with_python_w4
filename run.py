#!/usr/bin/env python3

#script to upload description and image to server
import os
import requests

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
		lines = openedFile.readlines()
		data["name"] = lines[0].strip("\n ")

print(data)


