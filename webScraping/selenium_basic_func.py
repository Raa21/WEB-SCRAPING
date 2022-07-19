# -*- coding: utf-8 -*-
"""
Created on Tue May 24 15:37:37 2022

@author: rajen
"""

from selenium import webdriver

driver = webdriver.Chrome("C:/Users/rajen/OneDrive/Desktop/webScraping/chromedriver.exe")

driver.get('https://www.goat.com/brand/air-jordan')


for i in range(1,15):
    
    price = driver.find_element_by_xpath('//*[@id="grid-body"]/div/div[1]/div['+str(i)+']/a/div[1]/div[2]/div').text
    print(price)
    
    


#text input

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:/Users/rajen/OneDrive/Desktop/webScraping/chromedriver.exe")

driver.get('https://www.google.co.in/')

box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('web scraping')
box.send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/div/a').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[1]/a[1]').click()
#driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()

driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()


#screenshot

driver = webdriver.Chrome("C:/Users/rajen/OneDrive/Desktop/webScraping/chromedriver.exe")

driver.get('https://www.google.co.in/')

box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('Lion')
box.send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
time.sleep(5)
#driver.save_screenshot('C:/Users/rajen/OneDrive/Desktop/webScraping/lion1.png')
driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[4]/a[1]/div[1]/img').screenshot('C:/Users/rajen/OneDrive/Desktop/webScraping/lion2.png')


#self scrolling

driver.execute_script('return document.body.scrollHeight')

while True:
    
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(5)
    #link = driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
    
    































