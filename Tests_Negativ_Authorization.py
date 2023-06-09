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
    pytest.driver.find_element(By.ID, 'kc-login').click
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'form-error-message'))
    )

    assert pytest.driver.find_elemet(By.ID, 'form-error-message')


def test_incorrect_autorizationapass(Rostelecom):
    pytest.driver.find_element(By.ID, 'username').send_keys('ip90m9mpc@qiott.com') # Валидная почта
    pytest.driver.find_element(By.ID, 'password').send_keys('Test00006') # Невалидный пароль
    pytest.driver.find_element(By.ID, 'kc-login').click
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'form-error-message'))
    )

    assert pytest.driver.find_elemet(By.ID, 'form-error-message')