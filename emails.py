#!/usr/bin/env python3

from email.message import EmailMessage
import mimetypes
import smtplib
import os.path

# email methods and functions

# email generate method with attachment
def generate_email(sender, recipient, subject, body, attachment):
    # generate the main email message
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)
    # generate the attachment mime types and complete the message
    attachment_path = attachment
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split("/", 1)
    # concat the attachment to message object
    with open(attachment_path, "rb") as attach_bin:
        message.add_attachment(attach_bin.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=attachment_filename)
    return message    

# email generate method for health_check.py

def generate_error_report(sender, recipient, subject, body):
    # here I changed the returned -message object- to error_message to avoid confusion
    error_message = EmailMessage()
    error_message["From"] = sender
    error_message["To"] = recipient
    error_message["Subject"] = subject
    error_message.set_content(body)
    return error_message


def send_email(message):
    # here create the email server and pass the message to send
    mail_server = smtplib.SMTP("localhost")
    mail_server.send_message(message)
    mail_server.quit()

