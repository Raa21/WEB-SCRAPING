# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:53:19 2022

@author: deepa
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = 'https://www.cricbuzz.com/cricket-series/4061/indian-premier-league-2022/points-table'
page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')
soup

table = soup.find('table',class_='table cb-srs-pnts')
table

headers = []
for i in table.find_all('tr')[0]:
    title = i.text
    headers.append(title)

df = pd.DataFrame(columns = headers)

table.find_all('td',class_ ='cb-srs-pnts-name')[5].text

name = []
for j in table.find_all('td',class_ ='cb-srs-pnts-name'):
    t = j.text
    name.append(t)
    
df1 = pd.DataFrame({'Team':name} )




for j in table.find_all('td', class_=' cb-srs-pnts-th'):
    r = j.find_all('td')
    row = [tr.text for tr in r]
    
df.loc[1] = row