# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 20:18:49 2022

@author: rajen
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
driver = webdriver.Chrome("C:/Users/rajen/OneDrive/Desktop/webScraping/chromedriver.exe")

driver.get('https://web.whatsapp.com/')
time.sleep(2)

sr = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
sr.send_keys('Rajendra')
sr.send_keys(Keys.ENTER)


words = ['cat','dog','cow','parrot','buffalo','maghia','banda','bia','betichod','bhaunighia','bedha']

for i in range(20):
    msg = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    msg.send_keys('You Phone Has Been hacked. This is just a demo ....................                 !!!!!!!!!YOUR   DEVICE   HAS BEEEM     HACKED HACKED HACKED HACKED HACKED HACKED !!!!!!!!!!!                    .............................................Send me 500rs to stop this hack or else your data will get deleted')
    msg.send_keys(Keys.ENTER)
    time.sleep(1)