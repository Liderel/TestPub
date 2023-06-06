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


otvetlist = 'ip90m9mpc@qiott.com'
login = 'ip90m9mpc'
domain = 'qiott.com'

def test_pass_change(Rostelecom):



    pytest.driver.find_element(By.ID, 'forgot_password').click()
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(otvetlist)
    time.sleep(20)
    pytest.driver.find_element(By.ID, 'reset').click()

    time.sleep(10)

    response = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}')

    messages = response.json()

    time.sleep(10)

    meskey = messages[0]['id']
    print(meskey)
    time.sleep(5)

    response = requests.get(
        f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={meskey}')
    text = response.json()
    print(text)
    time.sleep(5)
    soup = BeautifulSoup(text['body'], 'html.parser')
    delenieotvet = soup.p.text.split(': ')[1].strip().split('.')[0]
    messaglist = list(delenieotvet)
    print(messaglist)

    pytest.driver.find_element(By.ID, 'rt-code-0').send_keys(messaglist[0])

    pytest.driver.find_element(By.ID, 'rt-code-1').send_keys(messaglist[1])

    pytest.driver.find_element(By.ID, 'rt-code-2').send_keys(messaglist[2])

    pytest.driver.find_element(By.ID, 'rt-code-3').send_keys(messaglist[3])

    pytest.driver.find_element(By.ID, 'rt-code-4').send_keys(messaglist[4])

    pytest.driver.find_element(By.ID, 'rt-code-5').send_keys(messaglist[5])

    time.sleep(15)

    pytest.driver.find_element(By.ID, 'password-new').send_keys(newpass)

    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(newpass)

    pytest.driver.find_element(By.ID, 't-btn-reset-pass').click()

    pytest.driver.find_element(By.ID, 'password').send_keys(newpass)