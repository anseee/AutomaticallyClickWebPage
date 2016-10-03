#-*- coding: utf-8 -*-
import time
from selenium import webdriver

YOUR_PAGE_URL = 'http://www.hanwhafireworks.com/event/main.do'

driver = webdriver.Firefox()
driver.get(YOUR_PAGE_URL)
time.sleep(1)
elem1 = driver.find_element_by_link_text("골든티켓 받기")
elem1.click()
time.sleep(1)
driver.find_element_by_xpath('//li[img/@src="./_resource/images/sns_face_icon.png"]').click()
time.sleep(1)
