# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:16:58 2022

@author: rajen
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome("C:/Users/rajen/OneDrive/Desktop/webScraping/chromedriver.exe")
driver.get('https://www.nike.com/in/w/mens-sale-3yaepznik1')
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

product_card = soup.find_all('div',class_='product-card__body')
#df  = pd.DataFrame({'Link':[''],'Title':[''],'Category':[''],'Price':[''],'SaLe Price':['']})

l = []
n = []
c = []
f = []
s = []


for product in product_card:
    
    try:
        link = product.find('a',class_='product-card__link-overlay').get('href')
        l.append(link)
        name = product.find('div',class_='product-card__title').text
        n.append(name)
        category = product.find('div',class_='product-card__subtitle').text
        c.append(category)
        full_price = product.find('div',class_='product-price is--striked-out').text.split()
        f.append(full_price)
        sale_price = product.find('div',class_='product-price is--current-price css-s56yt7').text.split()
        s.append(sale_price)
        
    except:
        pass
    
        
    
df  = pd.DataFrame({'Link':l,'Title':n,'Category':c,'Price':f,'SaLe Price':s})
df.to_csv('C:/Users/rajen/OneDrive/Desktop/webScraping/nike_men_sale2.csv')