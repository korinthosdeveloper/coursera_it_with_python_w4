#!/usr/bin/env python3

#reports py to make the pdf report

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(paragraph, title, file_path):
    styles = getSampleStyleSheet()
    report_title = Paragraph(title)
    report_body = Paragraph(paragraph)
    report = SimpleDocTemplate(file_path)
    report.buil([report_title,	report_body])



