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

otvetlist = ''
login = ''
domain = ''


def test_registration(Rostelecom):
    # Тест на валидную регистрацию


    response = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox')

    time.sleep(2)
    #
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
        time.sleep(2)
    #
    # pytest.driver.find_element(By.ID, 'rt-code-0').send_keys(messaglist[0])
    #
    # pytest.driver.find_element(By.ID, 'rt-code-1').send_keys(messaglist[1])
    #
    # pytest.driver.find_element(By.ID, 'rt-code-2').send_keys(messaglist[2])
    #
    # pytest.driver.find_element(By.ID, 'rt-code-3').send_keys(messaglist[3])
    #
    # pytest.driver.find_element(By.ID, 'rt-code-4').send_keys(messaglist[4])
    #
    # pytest.driver.find_element(By.ID, 'rt-code-5').send_keys(messaglist[5])

    time.sleep(5)

    return otvetlist, login, domain

