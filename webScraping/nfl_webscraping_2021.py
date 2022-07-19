# -*- coding: utf-8 -*-
"""
Created on Mon May 23 11:47:32 2022

@author: rajen
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nfl.com/standings/league/2021/REG'
page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')
soup

table = soup.find('table',{'summary':'Standings - Detailed View'})
table


header = []
for i in table.find_all('th'):
    t = i.text
    header.append(t)
    
df = pd.DataFrame(columns = header)


for row in table.find_all('tr')[1:]:
    first_data = row.find_all('td')[0].find('div',class_='d3-o-club-fullname').text.strip()
    data = row .find_all('td')[1:]
    row_data = [td.text for td in data]
    row_data.insert(0,first_data)
    length = len(df)
    df.loc[length] = row_data
    
df.to_csv('C:/Users/rajen/OneDrive/Desktop/webScraping/nfl_2021_table.csv')
