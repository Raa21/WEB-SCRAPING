# -*- coding: utf-8 -*-
"""
Created on Mon May 23 12:38:16 2022

@author: rajen
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.carpages.ca/used-cars/search/?category_id=1'
page = requests.get(url)
page

soup = BeautifulSoup(page.text,'lxml')
soup

link = []
price = []
title = []
kms = []
color = []
counter = 0

while counter < 18:

    data = soup.find_all('div',class_='media soft push-none rule')
    
    for d in data:
        links = d.find('a').get('href')
        l = 'https://www.carpages.ca/'+ links
        link.append(l)
        
        p = d.find('strong',class_='delta').text.split()
        price.append(p)
        
        t = d.find('h4')
        ti =t.find('a').text
        title.append(ti)
        
        km = d.find_all('div',class_='grey l-column l-column--small-6 l-column--medium-4')[0].text.strip()
        kms.append(km)
        
        co = d.find_all('div',class_ ='grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
        color.append(co)
        
    next_page = soup.find('a',class_='nextprev').get('href')
    next_full = 'https://www.carpages.ca/'+ next_page
    url = next_full
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'lxml')
    counter += 1
    
df = pd.DataFrame({'Links':link,
                   'Title':title,
                   'Price':price,
                   'KM covered':kms,
                   'Color':color })
df.to_csv('C:/Users/deepa/Desktop/WebScraping/cars_scraping.csv')
df.to_csv('C:/Users/rajen/OneDrive/Desktop/webScraping//convertible_cars_scraping.csv')