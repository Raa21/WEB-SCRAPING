# -*- coding: utf-8 -*-
"""
Created on Mon May 30 17:35:34 2022

@author: rajen
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

driver =  webdriver.Chrome("C:/Users/rajen/OneDrive/Desktop/webScraping/chromedriver.exe")
driver.get('https://in.linkedin.com/?trk=IN-SEM_google-adwords_Jordan-brand-sign-up&mcid=6844056167778418688&trk2=ga_campid=14650114791_asid=127961666580_crid=545833659343_kw=linkedin_d=c_tid=kwd-285981853_n=g_mt=p_geo=1007799_slid=&gclid=Cj0KCQjw1tGUBhDXARIsAIJx01nou3nM9X0gStflfpAquBVpZ0m-UyhaLq8soAojtvnOauAJ6AvR_D8aAr0OEALw_wcB&gclsrc=aw.ds')
time.sleep(3)

driver.find_element_by_xpath('/html/body/nav/ul/li[4]/a').click()
time.sleep(2)

search = driver.find_element_by_xpath('/html/body/div[1]/header/nav/section/section[2]/form/section[1]/input')
search.send_keys('Business Analyst')
search.send_keys(Keys.ENTER)
time.sleep(3)
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    break


soup = BeautifulSoup(driver.page_source,'lxml')
all_jobs = soup.find('a',class_='empty-results-pivot__see-all-jobs-cta-link').get('href')
driver.get(all_jobs)
time.sleep(2)
soup = BeautifulSoup(driver.page_source,'lxml')
postings = soup.find_all('div',class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
 

l = []
j = []
c = []
lc = []
da = []
c_link = []


while True:
    for post in postings:
        link = post.find('a',class_='base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]').get('href')
        l.append(link)
        
        job = post.find('h3',class_='base-search-card__title').text.strip()
        j.append(job)
        
        company = post.find('h4',class_='base-search-card__subtitle').text.strip()
        c.append(company)
        
        company_link = post.find('a',class_='hidden-nested-link').get('href')
        c_link.append(company_link)
        
        loc = post.find('span',class_='job-search-card__location').text.strip()
        lc.append(loc)
        
        day = post.find('time',class_= re.compile('job-search-card__listdate')).text.strip()
        da.append(day)
        
        
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source,'lxml')
    postings = soup.find_all('div',class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
    ls = list(set(l))
    
    if len(ls) > 100:
        break