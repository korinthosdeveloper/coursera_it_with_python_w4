#!/usr/bin/env python3

# make the report body here

import os
import datetime
import reports

time_stamp = datetime.datetime.now().strftime("%Y-%m-%d")

user = os.getenv("USER")
path = ("/home/{}/supplier_description/".format(user))

#change the path here
attachment = "/home/{}/project1/processed.pdf".format(user)

textDir = os.listdir(path)
paragraph = ""

for file in textDir:
    with open(path+file, "r") as openedFile:
        lines = openedFile.readlines()
        paragraph += "name: " + lines[0].strip("\n ") + "<br/>"  + "weight: " +  lines[1].strip("\n ") + "<br/>" + "<br/>" 



if __name__ == "__main__":
    title = "Process Updated on " + time_stamp
    reports.generate_report(title, paragraph, attachment)
