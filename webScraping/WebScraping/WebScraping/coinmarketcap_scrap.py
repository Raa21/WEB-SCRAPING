# -*- coding: utf-8 -*-
"""
Created on Wed May  4 22:19:36 2022

@author: deepa
"""

import requests
from bs4 import BeautifulSoup

url = 'https://coinmarketcap.com/currencies/terra-luna/'
page = requests.get(url)
page

soup = BeautifulSoup(page.text,'lxml')
soup


name = soup.find('h2',class_ = 'sc-1q9q90x-0 jCInrl h1').text
name

price = soup.find('div', class_='priceValue').text
price

price_chg = soup.find('span',class_ = 'sc-15yy2pl-0 gEePkg')
price_chg

nested = soup.find_all('div',class_ = 'hide statsContainer')[0]

mc_nest = nested.find_all('div',class_ = 'statsBlock')[0]

mc = mc_nest.find('div',class_ = 'statsValue').text
mc

vol_nest = nested.find_all('div',class_ = 'statsBlock')[2]
vol_nest1 = vol_nest.find_all('div',class_ = 'statsBlockInner')[0]

vol = vol_nest1.find('div',class_ = 'statsValue').text
vol