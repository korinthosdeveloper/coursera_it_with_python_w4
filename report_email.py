#!/usr/bin/env python3

# make the report body here

import os
import datetime
import reports
import emails

# get time
time_stamp = datetime.datetime.now().strftime("%Y-%m-%d")
#get user to find the directory and path
user = os.getenv("USER")
path = ("/home/{}/supplier-data/description/".format(user))

#change the path here
attachment = "/home/{}/tmp/processed.pdf".format(user)
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

    # here is the code to generate the email and send it
    email_sender = "automation@example.com"
    email_to = "student_username@example.com"
    email_subject = "Upload Completed - Online Fruit Store"
    email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    email_attachment = attachment
    # call emails.py generate_email method, dont forget that this method returns a message obj
    message = emails.generate_email(email_sender, email_to, email_subject, email_body, email_attachment)

    # here call emails.py send_email method to finally send the report over internet
    emails.send_email(message)
