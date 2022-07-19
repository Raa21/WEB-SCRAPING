# -*- coding: utf-8 -*-
"""
Created on Wed May 11 17:47:27 2022

@author: deepa
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7'
page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')


l = []
ti = []
p = []
kms =[]
color = []
counter = 0

while counter<10:
    postings = soup.find_all('div',class_ = 'media soft push-none rule')
    postings
    

    for post in postings:
        
        link = post.find('a').get('href')
        link_full = 'https://www.carpages.ca' + link
        l.append(link_full)
        
        t = post.find('h4')
        t1 = t.find('a').get('title')
        ti.append(t1)
        
        price = post.find('strong',class_ ='delta').text.strip()
        p.append(price)
        
        km = post.find_all('div',class_ ='grey l-column l-column--small-6 l-column--medium-4')[0].text.strip()
        kms.append(km)
        
        co = post.find_all('div',class_ ='grey l-column l-column--small-6 l-column--medium-4')[1].text.split()
        color.append(co)
        
    next_page = soup.find('a',class_='nextprev').get('href')
    next_page_full = 'https://www.carpages.ca' + next_page
    url = next_page_full
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'lxml')
    counter += 1
    
    
df = pd.DataFrame({'Car Name':ti,'link':l,'Price':p,'KMS Covered':kms,'Colour':color})
df.to_csv('C:/Users/deepa/Desktop/WebScraping/cars_scraping.csv')