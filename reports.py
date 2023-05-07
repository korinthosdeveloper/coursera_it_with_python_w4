#!/usr/bin/env python3

#reports py to make the pdf report

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()
report = SimpleDocTemplate("processed.pdf")


def generate_report(paragraph, title, file_path):
    report_title = title
    report_body = paragraph
    attachment = file_path



