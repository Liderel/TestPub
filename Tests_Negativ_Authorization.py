import pytest
import time
import requests
import json
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from settings import *

def test_incorrect_autorizationall(Rostelecom):
    pytest.driver.find_element(By.ID, 'username').send_keys('v9nvas7mmj@kzccv.com') # Невалидная почта
    pytest.driver.find_element(By.ID, 'password').send_keys('Test00006') # Невалидный пароль

    if (pytest.driver.find_elements(By.ID, 'captcha')):
        time.sleep(20)
    else:
        pass
    pytest.driver.find_element(By.ID, 'kc-login').click()

    error_mess = pytest.driver.find_element(By.ID, 'form-error-message')

    assert error_mess.text == 'Неверный логин или пароль'


def test_incorrect_autorizationapass(Rostelecom):
    pytest.driver.find_element(By.ID, 'username').send_keys('ip90m9mpc@qiott.com') # Валидная почта
    pytest.driver.find_element(By.ID, 'password').send_keys('Test00006') # Невалидный пароль
    # Время ожидание на случай необходимости ввода кода с картинки
    time.sleep(10)
    pytest.driver.find_element(By.ID, 'kc-login').click()

    error_mess = pytest.driver.find_element(By.ID, 'form-error-message')

    assert error_mess.text == 'Неверный логин или пароль'