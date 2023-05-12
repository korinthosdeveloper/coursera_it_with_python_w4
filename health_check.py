#!/usr/bin/env python3

import emails
import os
import psutil
import shutil
import socket

# email construction
sender = "automation@example.com"
recipient = "{}@example.com".format(os.environ["USER"])
subject = ""
body = "Please check your system and resolve the issue as soon as possible."

# check cpu usage
cpu_usage = psutil.cpu_percent(1)
# check disk usage
disk_usage = shutil.disk_usage("/")
disk_total = disk_usage.total
disk_in_use = disk_usage.used
disk_threshold = (disk_in_use / disk_total) * 100
# check memory usage
mem_available = psutil.virtual_memory().available
mem_available_MB = (mem_available / 1024) ** 2
# check localost ip address
local_host = socket.gethostbyname("localhost")

# if cpu uses more than 80% alert
if cpu_usage > 80:
    subject = "Error - CPU usage is over 80%"
# if disk is use more than 80% of disk space alert
elif disk_threshold < 20:
    subject = "Error - Available disk space is less than 20%"      
# if free memory less than 500 MB alert
elif mem_available_MB < 500:
    subject = "Error - Available memory is less than 500MB"
# if local host ip is not equal to 127.0.0.1 alert
elif local_host != "127.0.0.1":
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
# send email only if we have problem!
if subject != "":
    # generate and send error_report email
    emails.send_email(emails.generate_error_report(sender, recipient, subject, body))
