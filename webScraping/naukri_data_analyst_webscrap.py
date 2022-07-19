# -*- coding: utf-8 -*-
"""
Created on Sat May 28 00:34:00 2022

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
driver.get('https://www.naukri.com/')
time.sleep(3)

search = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div/div/div[1]/div/div/div/input')
search.send_keys('image processing')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div/div/div[6]').click()
time.sleep(3)

#driver.find_element_by_xpath('//*[@id="root"]/div[3]/div[2]/section[1]/div[2]/div[1]/div[2]/div/label/i').click()
#time.sleep(2)

j = []
c = []
l = []
s = []
d = []
desc = []
lc = []
sk = []
counter = 0

while counter < 5:
    soup = BeautifulSoup(driver.page_source,'lxml')
    postings = soup.find_all('article',class_='jobTuple bgWhite br4 mb-8')
    
    for post in postings:
        
        link = post.find('a',class_='title fw500 ellipsis').get('href')
        l.append(link)
        
        company = post.find('a',class_='subTitle ellipsis fleft').text
        c.append(company)
        
        title = post.find('a',class_='title fw500 ellipsis').text
        j.append(title)
        
      
        
        try:
            salary = post.find('li',class_='fleft grey-text br2 placeHolderLi salary').text
            s.append(salary)
            
            loc = post.find('li',class_='fleft grey-text br2 placeHolderLi location').text
            lc.append(loc)
            
            date = post.find('li',class_='fleft grey-text br2 placeHolderLi experience').text
            d.append(date)
            
        except:
            
            date = 'N/A'
            d.append(date)
            
            
        
        des = post.find('div',class_='job-description fs12 grey-text').text
        desc.append(des)
        
        qual = post.find_all('li',class_='fleft fs12 grey-text lh16 dot')
        qu = []
        for i in qual:
            q = i.text
            qu.append(q)
        sk.append(qu)
        
    counter += 1
        
    try:
        button = soup.find('a',class_='fright fs14 btn-secondary br2').get('href')
        driver.get('https://www.naukri.com'+button)
        time.sleep(2)
       
        
    except:
        break

df = pd.DataFrame({'Link':l,'Job Title':j,'Company Name':c,'Experience':d,'Salary':s,'Description':desc,'Skills Required':sk})
df.to_csv('C:/Users/rajen/OneDrive/Desktop/webScraping/naukri_job_search_image_processing.csv')

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
part.set_payload(open('C:/Users/rajen/OneDrive/Desktop/webScraping/naukri_job_search_image_processing.csv', 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename ="naukri_job_search_image_processing.csv"')
msg.attach(part)

#Will login to your email and actually send the message above to the receiver
s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
s.login(user = 'forprojects5545@gmail.com', password = 'OD02BL5545')
s.sendmail(sender, receiver, msg.as_string())
s.quit()     
