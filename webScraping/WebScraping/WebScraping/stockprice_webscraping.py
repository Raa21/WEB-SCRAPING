import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

url  = 'https://www.marketwatch.com/investing/index/tsla'

page = requests.get(url)
#page.text

soup = BeautifulSoup(page.text,'lxml')
#soup


price = soup.find('bg-quote',class_ = re.compile('value') )
price

close_price = soup.find('td',class_ = 'table__cell u-semi')
close_price

nested = soup.find_all('div',class_ = 'range__header')[2]
nested

lower =  nested.find_all('span',class_ = 'primary')[0]
lower

upper = nested.find_all('span',class_ = 'primary')[1]
upper

rating = soup.find('li' ,class_ = 'analyst__option active')
rating

name = soup.find('h1',class_ = 'company__name')
name

name_list = []
for i in name:
    name2 = i.text
    name_list.append(name2)
    
price_list = []
for i in price:
    price2 = i.text
    price_list.append(price2)
    
close_price_list = []
for i in close_price:
    close_price2 = i.text
    close_price_list.append(close_price2)
    
rating_list = []
for i in rating:
    rating2 = i.text
    rating_list.append(rating2)
    
upper_list = []
for i in upper:
    upper2 = i.text
    upper_list.append(upper2)
    
    
lower_list = []
for i in lower:
    lower2 = i.text
    lower_list.append(lower2)
    


table = pd.DataFrame({'Company Name':name,
                      'Price':price,
                      'Close Price':close_price,
                      'Lower':lower,
                      'Upper':upper,
                      'Rating':rating},index=[1])
table