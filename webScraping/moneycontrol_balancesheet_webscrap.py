# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 19:17:00 2022

@author: rajen
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.moneycontrol.com/financials/itc/balance-sheetVI/ITC#ITC'
page = requests.get(url)


soup = BeautifulSoup(page.text,'lxml')
soup

table = soup.find('table',class_='mctable1')
table

header = []
head = table.find_all('tr',class_='lightbg')[0]

for i in head.find_all('td'):
    h = i.text
    header.append(h)
    
df = pd.DataFrame(columns = header)

for row in table.find_all('tr')[1:]:
    first_data = row.find_all('td')[0].text
    data = row.find_all('td')[1:]
    try:
        row_data = [td.text for td in data]
        
    except:
        row_data = ['NA' for td in data]
        
    row_data.insert(0,first_data)
    length = len(df)
    df.loc[length] = row_data


df.to_csv('C:/Users/rajen/OneDrive/Desktop/webScraping/moneycontro_balancesheet_itc.csv')

 