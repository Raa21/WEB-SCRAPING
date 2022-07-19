# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:44:52 2022

@author: deepa
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nfl.com/standings/league/2019/REG'
page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')


table = soup.find('table',{'summary' : 'Standings - Detailed View'})

table.find_all('th')

headers = []

for i in table.find_all('th')[0:]:
    title = i.text
    headers.append(title)
    
    
df = pd.DataFrame(columns = headers)

row_data = table.find_all('tr')[1:]


for j in row_data:
    r = j.find_all('td')
    row = [tr.text for tr in r]
    length = len(df)
    df.loc[length] = row
    
    
df.to_csv('C:/Users/deepa/Desktop/WebScraping/nfl_2019_table.csv')