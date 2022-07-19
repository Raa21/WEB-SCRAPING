# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:13:04 2022

@author: rajen
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("C:/Users/rajen/OneDrive/Desktop/webScraping/chromedriver.exe")

driver.get('https://www.facebook.com/')
time.sleep(1)
box = driver.find_element_by_xpath('//*[@id="email"] ')
box.send_keys('rajendrabera.raja96@gmail.com')
time.sleep(2)
pas = driver.find_element_by_xpath('//*[@id="pass"]')
pas.send_keys('OD02BL5545')
time.sleep(2)
pas.send_keys(Keys.ENTER)