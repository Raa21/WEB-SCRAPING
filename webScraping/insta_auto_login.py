# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:30:14 2022

@author: rajen
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("C:/Users/rajen/OneDrive/Desktop/webScraping/chromedriver.exe")

driver.get('https://www.instagram.com/?hl=en')
time.sleep(2)
box = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
box.send_keys('forprojects5545@gmail.com')
time.sleep(1)
pas = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
pas.send_keys('OD02BL5545')
time.sleep(1)
pas.send_keys(Keys.ENTER)
time.sleep(5)
ser = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
ser.send_keys('elon musk')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()
time.sleep(5)

#status
#driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/div/div/span/img').click()
#time.sleep(1)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a').click()
time.sleep(12)
driver.find_element_by_xpath('/html/body/div[6]/div[1]/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[2]/a').click()
time.sleep(7)
for j in range(1,25):
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[2]/button').click()
    time.sleep(7)
        
