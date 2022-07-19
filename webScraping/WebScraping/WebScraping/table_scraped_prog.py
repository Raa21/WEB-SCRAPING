# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:13:29 2022

@author: deepa
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/'
page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')
soup

table = soup.find('table',class_ = 'table table-striped table-bordered table-hover table-condensed table-list')
table

table.find_all('th')

headers = []
for i in table.find_all('th'):
    title = i.text
    headers.append(title)
    
dframe = pd.DataFrame(columns = headers)


table.find_all('tr')[1:]

for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [tr.text for tr in row_data]
    length  = len(dframe)
    dframe.loc[length] = row


dframe.to_csv('C:/Users/deepa/Desktop/WebScraping/table_scraped.csv')