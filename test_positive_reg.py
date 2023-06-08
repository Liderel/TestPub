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



def test_registration(Rostelecom):
    # Тест на валидную регистрацию


    response = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox')

    time.sleep(2)

    otvet = response.json()
    otvetlist = otvet[0]
    login = otvetlist.split('@')[0]
    domain = otvetlist.split('@')[1]
    print(otvet)
    time.sleep(3)



    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(Name)

    # Ввод Фамилий
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Familiya)

    # Ввод Почты
    pytest.driver.find_element(By.ID, 'address').send_keys(otvet)

    # ВВод пароля с без спецсимволов или больших букв: Переменная - Passnobig
    # Ввод Пароля
    pytest.driver.find_element(By.ID, 'password').send_keys(Pass)

    # Ввод потверждения Проля
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(Pass)

    # Нажатие Регистрироваться
    pytest.driver.find_element(By.NAME, 'register').click()

    time.sleep(30)

    response = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}')

    messages = response.json()

    time.sleep(25)


    meskey = messages[0]['id']
    print(meskey)
    time.sleep(5)

    response = requests.get(
        f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={meskey}')
    text = response.json()
    print(text)
    time.sleep(5)
    soup = BeautifulSoup(text['body'], 'html.parser')
    delenieotvet = soup.p.text.split(': ')[1].strip()
    messaglist = list(delenieotvet)
    print(messaglist)

    for i, x in enumerate(messaglist):
        pytest.driver.find_element(By.ID, f'rt-code-{i}').send_keys(x)

    time.sleep(5)
    print(otvet)

    return otvet

def test_autorization(Rostelecom):
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(Mail)
    pytest.driver.find_element(By.ID, 'password').send_keys(Pass)
    pytest.driver.find_element(By.ID, 'kc-login').click()



