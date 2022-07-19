# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:49:57 2022

@author: rajen
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("C:/Users/rajen/OneDrive/Desktop/webScraping/chromedriver.exe")

driver.get('https://www.google.co.in/')

box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('top 100 movies all time')
box.send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element_by_xpath('//*[@id="rso"]/div[1]/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/a').click()
time.sleep(3)

driver.execute_script('window.scrollTo(0,5000)')
time.sleep(3)
driver.save_screenshot('C:/Users/rajen/OneDrive/Desktop/webScraping/seven7.png')

driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div[25]/div[2]/a/img').screenshot('C:/Users/rajen/OneDrive/Desktop/webScraping/seven72.png')