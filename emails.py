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

def send_email():
    pass

