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
from test_positive_reg import test_registration



def test_pass_change(Rostelecom, test_registration):



    pytest.driver.find_element(By.ID, 'forgot_password').click()
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(test_registration.otvetlist)
    time.sleep(20)
    pytest.driver.find_element(By.ID, 'reset').click()

    time.sleep(10)

    response = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={test_registration.login}&domain={test_registration.domain}')

    messages = response.json()

    time.sleep(10)

    meskey = messages[0]['id']
    print(meskey)
    time.sleep(5)

    response = requests.get(
        f'https://www.1secmail.com/api/v1/?action=readMessage&login={test_registration.login}&domain={test_registration.domain}&id={test_registration.meskey}')
    text = response.json()
    print(text)
    time.sleep(5)
    soup = BeautifulSoup(text['body'], 'html.parser')
    delenieotvet = soup.p.text.split(': ')[1].strip().split('.')[0]
    messaglist = list(delenieotvet)
    print(messaglist)

    for i, x in enumerate(messaglist):
        pytest.driver.find_element(By.ID, f'rt-code-{i}').send_keys(x)

    time.sleep(15)

    pytest.driver.find_element(By.ID, 'password-new').send_keys(newpass)

    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(newpass)

    pytest.driver.find_element(By.ID, 't-btn-reset-pass').click()

    pytest.driver.find_element(By.ID, 'password').send_keys(newpass)