# -*- coding: utf-8 -*-
"""
Created on Sun May 29 18:55:29 2022

@author: rajen
"""

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Input the email account that will send the email and who will receiving it
sender = 'foeprojects5545@gmail.com'
receiver = 'rajendrabera.raja96@gmail.com'

#Creates the Message, Subject line, From and To
msg = MIMEMultipart()
msg['Subject'] = 'New Jobs on Indeed'
msg['From'] = sender
msg['To'] = ','.join(receiver)

#Adds a csv file as an attachment to the email (indeed_jobs.csv is our attahced csv in this case)
part = MIMEBase('application', 'octet-stream')
part.set_payload(open('C:/Users/rajen/OneDrive/Desktop/webScraping/indeed_job_search_data_analysis.csv', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename ="indeed_job_search_data_analysis.csv"')
msg.attach(part)

#Will login to your email and actually send the message above to the receiver
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = 'forprojects5545@gmail.com', password = 'OD02BL5545')
s.sendmail(sender, receiver, msg.as_string())
s.quit()