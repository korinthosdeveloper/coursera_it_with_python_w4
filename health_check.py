#!/usr/bin/env python3

import emails



# placholders for the email construction
sender = ""
recipient = ""
subject = ""
body = ""


# generate and send error_report email
emails.send_email(emails.generate_error_report(sender, recipient, subject, body))