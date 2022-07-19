# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:41:07 2022

@author: rajen
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome("C:/Users/rajen/OneDrive/Desktop/webScraping/chromedriver.exe")
driver.get('https://www.oyorooms.com/search?location=Shimla%2C%20Himachal%20Pradesh%2C%20India&city=Shimla&searchType=city&coupon=&checkin=08%2F06%2F2022&checkout=13%2F06%2F2022&roomConfig%5B%5D=2&guests=2&rooms=1&countryName=India&country=india&filters%5Bcity_id%5D=59')
time.sleep(3)

last_height = driver.execute_script('return document.body.scrollHeight')

while True:
   
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div[3]/section/div/div[3]/div').click()
    time.sleep(4)
    new_height = driver.execute_script('return document.body.scrollHeight')
        
    if new_height == last_height:
        break
    last_height = new_height
        

    
soup = BeautifulSoup(driver.page_source,'lxml')

product_card = soup.find_all('div',class_='oyo-row oyo-row--no-spacing hotelCardListing')

#df  = pd.DataFrame({'Link':[''],'Title':[''],'Category':[''],'Price':[''],'SaLe Price':['']})

l = []
n = []
c = []
f = []
s = []
st = []
st1 = []


for product in product_card:
    
    link = product.find('a',class_='c-nn640c u-width100').get('href')
    full_link = 'https://www.oyorooms.com/' + link
    l.append(full_link)
    name = product.find('h3',class_='listingHotelDescription__hotelName d-textEllipsis').text
    n.append(name)
    ad = product.find('span',class_='u-line--clamp-2').text
    c.append(ad)
    full_price = product.find('span',class_='listingPrice__slashedPrice d-body-lg').text
    f.append(full_price)
    sale_price = product.find('span',class_='listingPrice__finalPrice').text
    s.append(sale_price)
    star = product.find_all('span',class_='d-body-sm d-textEllipsis')
    for i in star:
        desc = i.text
        st1.append(desc)
    st.append(st1)
    st1 = []
    
        
df = pd.DataFrame({'Link':l,'Name':n,'Location':c,'Price':f,'Sale Price':s,'Description':st})
df.to_csv('C:/Users/rajen/OneDrive/Desktop/webScraping/oyo_shimla_webscrap.csv')