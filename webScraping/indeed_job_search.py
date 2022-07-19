# -*- coding: utf-8 -*-
"""
Created on Fri May 27 20:40:16 2022

@author: rajen
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import time

driver =  webdriver.Chrome("C:/Users/rajen/OneDrive/Desktop/webScraping/chromedriver.exe")
driver.get('https://in.indeed.com/?aceid=')
time.sleep(3)

job = driver.find_element_by_xpath('//*[@id="text-input-what"]')
job.send_keys('Cyber security')
time.sleep(1)
#loc = driver.find_element_by_xpath('//*[@id="text-input-where"]')
#loc.send_keys('Bhubaneswar')
#time.sleep(1)
#loc.send_keys(Keys.ENTER)
driver.find_element_by_xpath('//*[@id="jobsearch"]/button').click()
time.sleep(3)


j = []
c = []
l = []
s = []
d = []
desc = []
lc = []
counter = 0

while counter < 5:
    soup = BeautifulSoup(driver.page_source,'lxml')
    postings = soup.find_all('div',class_='slider_container css-11g4k3a eu4oa1w0')

    for post in postings:
            
        link = post.find('a',class_='jcs-JobTitle').get('href')
        full_link = 'https://in.indeed.com'+ link
        l.append(full_link)
        job = post.find('h2',class_='jobTitle').text
        j.append(job)
        company = post.find('span',class_='companyName').text
        c.append(company)
        try:
            loc = post.find('div',class_='companyLocation').text
            lc.append(loc)
            sal = post.find('div',class_='metadata salary-snippet-container').text
            s.append(sal)
        except:
            loc = 'N/A'
            sal = 'N/A'
            s.append(sal)
            lc.append(loc)
            
        date = soup.find('span',class_='date').text
        d.append(date)
          
    counter += 1
    try:
        button = soup.find('a',{'aria-label':'Next'}).get('href')
        driver.get('https://in.indeed.com'+button)
        time.sleep(1)
        
    except:
        break
        

df = pd.DataFrame({'Link':l,'Job Title':j,'Company Name':c,'Salary':s,'Date of Posting':d})
df.to_csv('C:/Users/rajen/OneDrive/Desktop/webScraping/indeed_job_search_cyber_security.csv')

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

#Input the email account that will send the email and who will receiving it
sender = 'foeprojects5545@gmail.com'
receiver = 'falgunidas0406@gmail.com'

#Creates the Message, Subject line, From and To
msg = MIMEMultipart()
msg['Subject'] = 'New Jobs on Indeed'
msg['From'] = sender
msg['To'] = ','.join(receiver)

#Adds a csv file as an attachment to the email (indeed_jobs.csv is our attahced csv in this case)
part = MIMEBase('application', 'octet-stream')
part.set_payload(open('C:/Users/rajen/OneDrive/Desktop/webScraping/indeed_job_search_cyber_security.csv', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename ="indeed_job_search_cyber_security.csv"')
msg.attach(part)

#Will login to your email and actually send the message above to the receiver
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = 'forprojects5545@gmail.com', password = 'OD02BL5545')
s.sendmail(sender, receiver, msg.as_string())
s.quit()     


