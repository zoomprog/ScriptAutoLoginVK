import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import config
s = Service(executable_path='/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
try:
    driver.maximize_window()#окно открывается на весь экран
    driver.get('https:/vk.com')
    email_input = driver.find_element(By.ID, 'index_email')
    email_input.clear()
    email_input.send_keys(config.data[0]['login'])
    email_input.send_keys(Keys.ENTER)
    time.sleep(5)
    password_input = driver.find_element(By.NAME, 'password')
    password_input.clear()
    password_input.send_keys(config.data[0]['password'])
    password_input.send_keys(Keys.ENTER)
    time.sleep(999)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
