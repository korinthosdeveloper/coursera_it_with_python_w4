#!/usr/bin/env python3

#reports py to make the pdf report

import datetime
import os
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet


styles = getSampleStyleSheet()
report = SimpleDocTemplate("processed.pdf")
report_title = Paragraph("Processed Update on ")

report.build([report_title])
