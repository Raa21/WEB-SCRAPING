# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:26:56 2022

@author: deepa
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.airbnb.co.in/s/Honolulu--HI--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=june&flexible_trip_dates%5B%5D=may&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Honolulu%2C%20HI%2C%20United%20States&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&checkin=2022-05-30&checkout=2022-06-04&source=structured_search_input_header&search_type=autocomplete_click'
page = requests.get(url)
page

soup = BeautifulSoup(page.text,'lxml')



t = []
p = []
tp = []
l =[]

while True:
    
    postings = soup.find_all('div',class_ = '_1e9w8hic')

    for post in postings:
        title = post.find('div',class_ ='kc26pza dir dir-ltr').text
        t.append(title)
        
        price = post.find('span',class_ ='_tyxjp1').text
        p.append(price)
        
        link = post.find('a',class_ = 'l8au1ct dir dir-ltr').get('href')
        link_full = 'https://www.airbnb.co.in' + link
        l.append(link_full)

        tot_price = post.find('div',class_ = '_tt122m').text
        tp.append(tot_price)
        
    next_page = soup.find('a',{'aria-label':'Next'}).get('href')
    next_page_full = 'https://www.airbnb.co.in' + next_page
    url1 = next_page_full
    page1 = requests.get(url1)
    soup1 = BeautifulSoup(page1.text,'lxml')
    