# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 17:11:37 2022

@author: rajen
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:/Users/rajen/OneDrive/Desktop/webScraping/chromedriver.exe")

driver.get('https://discord.com/login')
time.sleep(2)

user = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input')
user.send_keys('rajendrabera.raja96@gmail.com')

passw = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input')
passw.send_keys('OD02BL5545')

driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[1]/div/div[2]/div/div[1]/nav/ul/div[2]/div[3]/div[1]/div[2]/div').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="channels"]/ul/li[4]/div/div/a').click()
time.sleep(2)


msg = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div/div[2]')
msg.send_keys('P!h ')
time.sleep(1)
msg.send_keys(Keys.ENTER)

msg2 = driver.find_element_by_xpath('//*[@id="message-accessories-990954875435241482"]/article/div/div[4]').text.split()
                                      
m = msg2[1].lower()
m_old = ''
if (m != m_old):
    
    msg3 = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div/div[2]')
    msg.send_keys('P!c ' + m)
    time.sleep(1)
    msg.send_keys(Keys.ENTER)
    m_old = m
    

    