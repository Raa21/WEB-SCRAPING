import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(url)
page

soup = BeautifulSoup(page.text,'lxml')
soup


#find

soup.find('header')
soup.find('div',{'class': 'container test-site'})

soup.find('h4',{'class':'pull-right price'})

soup.find('h4',{'class':'pull-right price'}).string




#findAll()

soup.find_all('h4',{'class':'pull-right price'})[6:]

soup.find_all('a',{'class':'title'})
soup.find_all('p',{'class':'pull-right'})

soup.find_all(['h','p'])
soup.find_all(id = True)

soup.find_all(string = 'Iphone')

import re

soup.find_all(string = re.compile('Nokia'))
soup.find_all('p',class_=re.compile('pull'))

soup.find_all('p',class_=re.compile('pull'),limit = 4)
soup.find_all(string = ['Iphone','Nokia X'])

soup.find_all(class_ = re.compile('pull'))
soup.find_all('h4',class_ = re.compile('pull'))



import pandas as pd

product_name = soup.find_all('a',class_ = 'title')
product_name

price = soup.find_all('h4',class_ = 'pull-right price')
price

reviews = soup.find_all('p',class_ = re.compile('pull'))
reviews

description = soup.find_all('p',class_ = 'description')
description


product_name_list = []
for i in product_name:
    name = i.text
    product_name_list.append(name)
    

price_list = []
for i in price:
    price2 = i.text
    price_list.append(price2)


reviews_list = []
for i in reviews:
    reviews2 = i.text
    reviews_list.append(reviews2)


description_list = []
for i in description:
    description2 = i.text
    description_list.append(description2)
    


table = pd.DataFrame({'Product Name':product_name_list,
                      'Description':description_list,
                      'Price':price_list,
                      'Reviews':reviews_list})
table





boxes = soup.find_all('div',class_ = 'col-sm-4 col-lg-4 col-md-4')[2]
boxes

boxes.find('a').text
boxes.find('p',class_ = re.compile('pull')).text
boxes.find('h4',class_ = 'price').text
boxes.find('p',class_ ='description' ).text

box2 = soup.find_all('ul',class_ = 'nav',id = 'side-menu')[0]
box2.find_all('li')[0].text