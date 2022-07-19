# -*- coding: utf-8 -*-
"""
Created on Tue May  3 16:10:54 2022

@author: deepa
"""

import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'

page = requests.get(url)
page.text

soup = BeautifulSoup(page.text,'lxml')

soup

#Tags

tag = soup.header.p

tag.string

soup.header.p.string

soup.div

#Attributes

tag = soup.header.a
tag
tag.attrs

tag['data-toggle']
tag['attribute_new']='this is a demo attribute'
tag.attrs

