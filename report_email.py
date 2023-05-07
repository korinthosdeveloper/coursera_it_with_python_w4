#!/usr/bin/env python3

# make the report body here

import os
import datetime
import reports

# get time
time_stamp = datetime.datetime.now().strftime("%Y-%m-%d")
#get user to find the directory and path
user = os.getenv("USER")
path = ("/home/{}/supplier_description/".format(user))

#change the path here
attachment = "/home/{}/project1/processed.pdf".format(user)
# dir of files
textDir = os.listdir(path)
paragraph = ""

for file in textDir:
    with open(path+file, "r") as openedFile:
        # read all lines
        lines = openedFile.readlines()
        # make the paragraph string by concat name, weight and line breaks
        paragraph += "name: " + lines[0].strip("\n ") + "<br/>"  + "weight: " +  lines[1].strip("\n ") + "<br/>" + "<br/>" 



if __name__ == "__main__":
    # title of report
    title = "Process Updated on " + time_stamp
    # finally generate the report
    reports.generate_report(title, paragraph, attachment)
