from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')
print('Nazwa strony', driver.title)
time.sleep(1)

try:
    username_field = driver.find_element('name', 'user-nameA')   #zła nazwa
except:
    print('nie znaleziono po "name", szukam po ID')
    username_field = driver.find_element('id', 'user-name')
username_field.clear()
username_field.send_keys('standard_user')

try:
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
except NoSuchElementException:
    print('nie znaleziono hasła')
    raise

password_field.clear()
password_field.send_keys('secret_sauce')

time.sleep(1)
login_button = driver.find_element('name', 'login-button')

if not login_button.get_attribute('disabled'):
    print('Przycisk aktywny')
    login_button.click()


time.sleep(1)
driver.get_screenshot_as_file('moj_screenshot.png')
driver.quit()