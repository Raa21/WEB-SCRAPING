# -*- coding: utf-8 -*-
"""
Created on Thu May 26 23:15:29 2022

@author: rajen
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome("C:/Users/rajen/OneDrive/Desktop/webScraping/chromedriver.exe")
driver.get('https://www.naukri.com/data-analyst-jobs?k=data%20analyst&wfhType=1&functionAreaIdGid=3&functionAreaIdGid=4&functionAreaIdGid=30')
time.sleep(3)

