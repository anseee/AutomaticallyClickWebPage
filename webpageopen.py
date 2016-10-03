#-*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from apscheduler.schedulers.blocking import BlockingScheduler

def move_web_page():
    YOUR_PAGE_URL = 'http://www.hanwhafireworks.com/event/main.do'

    driver = webdriver.Chrome()
    driver.get(YOUR_PAGE_URL)
    time.sleep(1)
    elem1 = driver.find_element_by_link_text("골든티켓 받기")
    elem1.click()
    time.sleep(1)
    driver.find_element_by_xpath('//li[img/@src="./_resource/images/sns_face_icon.png"]').click()
    time.sleep(1)
    driver.switch_to_window(driver.window_handles[-1])
    title=driver.title
    time.sleep(1)
    username = driver.find_element(By.ID, value="email")
    username.send_keys("")
    time.sleep(1)
    password = driver.find_element(By.ID, value="pass")
    password.send_keys("")
    time.sleep(1)
    login = driver.find_element(By.ID, value="loginbutton")
    login.click()

scheduler = BlockingScheduler()
scheduler.add_job(move_web_page, 'interval', hours=1)
scheduler.start()
