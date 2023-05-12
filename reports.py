#!/usr/bin/env python3

#reports.py to make the pdf report

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

#function to generate the pdf file
#we call it from another file 

def generate_report(title, paragraph, file_path):
    # filename of pdf file
    report = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()
    # title of pdf
    report_title = Paragraph(title, styles["h1"])
    # main body
    report_body = Paragraph(paragraph, styles["BodyText"])
    # simple trick to have an empty line inside the pdf file
    empty_line = Spacer(1, 20)
    # create the pdf report file
    report.build([report_title, empty_line,report_body, empty_line])



