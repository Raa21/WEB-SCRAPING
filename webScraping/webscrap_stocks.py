# -*- coding: utf-8 -*-
"""
Created on Mon May 23 11:04:01 2022

@author: rajen
"""

import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.marketwatch.com/investing/stock/tsla?mod=search_symbol'
page = requests.get(url)


soup = BeautifulSoup(page.text,'lxml')
soup

name = soup.find('h1',class_='company__name').text
name

price = soup.find('bg-quote',class_='value').text
price

cl_price = soup.find('td',class_='table__cell u-semi').text
cl_price

r = soup.find('mw-rangebar',class_='element element--range range--yearly')

lower = r.find_all('span',class_='primary')[0].text
lower

upper = r.find_all('span',class_='primary')[1].text
upper

rating = soup.find('li',class_='analyst__option active').text
rating

