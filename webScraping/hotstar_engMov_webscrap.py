# -*- coding: utf-8 -*-
"""
Created on Thu May 26 22:14:32 2022

@author: rajen
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome("C:/Users/rajen/OneDrive/Desktop/webScraping/chromedriver.exe")
driver.get('https://www.hotstar.com/in/movies/languages/english')
time.sleep(3)

last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height
    
soup = BeautifulSoup(driver.page_source,'lxml')

sec = soup.find_all('div',class_='normal')
l = []
n = []
d = []
su = []
des = []

for s in sec:
    link = s.find('a').get('href')
    full_link = 'https://www.hotstar.com/' + link
    l.append(full_link)
    
    name = s.find('span',class_='content-title ellipsise').text
    n.append(name)
    
    dur = s.find('div',class_='dur show-gradient').text
    d.append(dur)
    
    sub = s.find('span',class_='subtitle').text
    su.append(sub)
    
    desc = s.find('div',class_='description ellipsize').text
    des.append(desc)
    
    
df = pd.DataFrame({'Link':l,'Movie Name':n,'Duration':d,'Genere':su,'Description':des})
df.to_csv('C:/Users/rajen/OneDrive/Desktop/webScraping/hotstar_EngMovie_webscrap.csv')