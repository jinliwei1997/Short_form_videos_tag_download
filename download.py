from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

# Please use your own account to avoid being banned by instagram.
username = 'jinliwei1998'
password = 'jlw260817'

if __name__ == '__main__':
    login_url = 'https://www.instagram.com/accounts/login/'
    driver = webdriver.Chrome()
    driver.get(login_url)
    time.sleep(3)
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']").click()
    time.sleep(3)
    driver.get('https://www.instagram.com/explore/tags/cat/')

