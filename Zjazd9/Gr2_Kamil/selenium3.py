from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as excon
from selenium2 import make_screenshot

def czekaj_na_id(element_id):
    timeout = 5
    timeout_message = f'Element o ID {element_id} nie pojawil sie w czasie {timeout} s.'
    lokalizator = (By.ID, element_id)
    znaleziono = excon.visibility_of_element_located(lokalizator)
    oczekiwator = WebDriverWait(driver, timeout)
    return oczekiwator.until(znaleziono, timeout_message)

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

try:
    login_button = czekaj_na_id('login-button')
except TimeoutException:
    print('Nie znaleziono')
    raise
else:
    print('znaleziono')
finally:
    print('zbieram screenshota i zamykam przegladarke')
    make_screenshot(driver)
    driver.quit()
    print('...koniec kodu...')