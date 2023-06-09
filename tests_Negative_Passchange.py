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

def test_incorect_passchange_short(Rostelecom):

    with open('mail.txt', 'r', encoding='UTF-8') as data_in:
        otvet = data_in.read()
        login = otvet.split('@')[0]
        domain = otvet.split('@')[1]

    pytest.driver.find_element(By.ID, 'forgot_password').click()
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(otvet)
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

    for i, x in enumerate(messaglist):
        pytest.driver.find_element(By.ID, f'rt-code-{i}').send_keys(x)

    time.sleep(15)

    pytest.driver.find_element(By.ID, 'password-new').send_keys('Test001')

    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('Test001')

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Длина пароля должна быть не менее 8 символов'

def test_incorect_passchange_nobig(Rostelecom):

    with open('mail.txt', 'r', encoding='UTF-8') as data_in:
        otvet = data_in.read()
        login = otvet.split('@')[0]
        domain = otvet.split('@')[1]

    pytest.driver.find_element(By.ID, 'forgot_password').click()
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(otvet)
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

    for i, x in enumerate(messaglist):
        pytest.driver.find_element(By.ID, f'rt-code-{i}').send_keys(x)

    time.sleep(15)

    pytest.driver.find_element(By.ID, 'password-new').send_keys('test00001')

    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('test00001')

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Пароль должен содержать хотя бы одну заглавную букву'


def test_incorect_passchange_nolatin(Rostelecom):
    with open('mail.txt', 'r', encoding='UTF-8') as data_in:
        otvet = data_in.read()
        login = otvet.split('@')[0]
        domain = otvet.split('@')[1]

    pytest.driver.find_element(By.ID, 'forgot_password').click()
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(otvet)
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

    for i, x in enumerate(messaglist):
        pytest.driver.find_element(By.ID, f'rt-code-{i}').send_keys(x)

    time.sleep(15)

    pytest.driver.find_element(By.ID, 'password-new').send_keys('Еуые0001')

    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('Еуые0001')

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Пароль должен содержать только латинские буквы'

def test_incorect_passchange_nonumbers(Rostelecom):
    with open('mail.txt', 'r', encoding='UTF-8') as data_in:
        otvet = data_in.read()
        login = otvet.split('@')[0]
        domain = otvet.split('@')[1]

    pytest.driver.find_element(By.ID, 'forgot_password').click()
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(otvet)
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

    for i, x in enumerate(messaglist):
        pytest.driver.find_element(By.ID, f'rt-code-{i}').send_keys(x)

    time.sleep(15)

    pytest.driver.find_element(By.ID, 'password-new').send_keys('Testtest')

    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('Testtest')

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'

def test_incorect_passchange_tolong(Rostelecom):
    with open('mail.txt', 'r', encoding='UTF-8') as data_in:
        otvet = data_in.read()
        login = otvet.split('@')[0]
        domain = otvet.split('@')[1]

    pytest.driver.find_element(By.ID, 'forgot_password').click()
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(otvet)
    # Время для ввода кода с картинки
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

    for i, x in enumerate(messaglist):
        pytest.driver.find_element(By.ID, f'rt-code-{i}').send_keys(x)

    time.sleep(15)

    pytest.driver.find_element(By.ID, 'password-new').send_keys('Testtesttesttesttest1')

    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('Testtesttesttesttest1')

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Длина пароля должна быть не более 20 символов'

def test_incorect_passchange_on_actual(Rostelecom):

    # Данный негативный тест должен производится после выполнения тестов Регистраций Авторизаций и смены пароля на новом аккаунте

    with open('mail.txt', 'r', encoding='UTF-8') as data_in:
        otvet = data_in.read()
        login = otvet.split('@')[0]
        domain = otvet.split('@')[1]

    pytest.driver.find_element(By.ID, 'forgot_password').click()
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.find_element(By.ID, 'username').send_keys(otvet)
    # Время для ввода кода с картинки
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

    for i, x in enumerate(messaglist):
        pytest.driver.find_element(By.ID, f'rt-code-{i}').send_keys(x)

    time.sleep(15)

    pytest.driver.find_element(By.ID, 'password-new').send_keys(newpass)

    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(newpass)

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Этот пароль уже использовался, укажите другой пароль'









