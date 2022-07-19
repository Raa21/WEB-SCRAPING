# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:46:28 2022

@author: rajen
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.99acres.com/search/property/rent/patia?city=162&locality=7728&keyword=patia&preference=R&area_unit=1&budget_min=0&res_com=R'
page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')
soup

data = soup.find_all('table',class_='srpTuple__tupleTable')

li = []
title = []
#esc = []
location = []

for d in data:
    
    l = d.find_all('td')[0]
    link = l.find('a').get('href')
    links = 'https://www.99acres.com/'+ link
    li.append(links)
    
    t = l.find('h2').text
    title.append(t)
    
   #price =d.find_all('tr')[2].text
   #desc.append(price)
    
    loc = d.find_all('tr')[4].text
    location.append(loc)
    
df = pd.DataFrame({'Links':li,
                   'Title':title,
                   'Locality':location})
df.to_csv('C:/Users/rajen/OneDrive/Desktop/webScraping/99acers_rent_scrap_patia.csv')