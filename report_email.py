#!/usr/bin/env python3

# make the report body here

import os
import datetime
import reports

attachment = "/tmp/processed.pdf"
time_stamp = datetime.datetime.now().strftime("%Y-%m-%d")

user = os.getenv("USER")
path = ("/home/{}/supplier_description/".format(user))
textDir = os.listdir(path)
paragraph = ""

for file in textDir:
    with open(path+file, "r") as openedFile:
        lines = openedFile.readlines()
        paragraph += lines[0].strip("\n ") + " <br> " + lines[1].strip("\n ") + " <br> " 

print(paragraph)

if __name__ == "__main__":
    pass
    #reports.generate_report(attachment, title, paragraph)
