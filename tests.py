import pytest
import time
import requests
import json
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# from MailReg import *
from settings import *




def test_Login(Rostelecom):
    # Вводим email
    pytest.driver.find_element(By.ID, 'username').send_keys(Mail)
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys(Pass)
    # Нажимаем Войти
    pytest.driver.find_element(By.ID, 'kc-login').click()

    assert pytest.driver.find_element(By.CLASS_NAME, 'user-avatar')


def test_Incorrect_Pass_Confirm_registration(Rostelecom):
    # Тест на не правильное потверждение пароля при регистрации

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(Name)

    # Ввод Фамилий
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Familiya)

    # Ввод Почты
    pytest.driver.find_element(By.ID, 'address').send_keys(Mail)

    # Ввод Пароля
    pytest.driver.find_element(By.ID, 'password').send_keys(Pass)

    # Ввод потверждения Проля
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(ErrorPass)

    # Нажатие Регистрироваться
    pytest.driver.find_element(By.NAME, 'register').click()

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta.rt-input-container__meta--error')))

    # Проверка на несовпадение паролей
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta.rt-input-container__meta--error')


def test_NoLatin_registration(Rostelecom):
    # Тест на валидную регистрацию

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(Name)

    # Ввод Фамилий
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Familiya)

    # Ввод Почты
    pytest.driver.find_element(By.ID, 'address').send_keys(Mail)

    # ВВод пароля с кирилицей: Переменная - Latinerrorpass
    # Ввод Пароля
    pytest.driver.find_element(By.ID, 'password').send_keys(Latinerrorpass)

    # Ввод потверждения Проля
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(Latinerrorpass)

    # Нажатие Регистрироваться
    pytest.driver.find_element(By.NAME, 'register').click()

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta.rt-input-container__meta--error')))

    # Проверка на несовпадение паролей
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta.rt-input-container__meta--error')


def test_NoBig_registration(Rostelecom):
    # Тест на валидную регистрацию

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(Name)

    # Ввод Фамилий
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Familiya)

    # Ввод Почты
    pytest.driver.find_element(By.ID, 'address').send_keys(Mail)

    # ВВод пароля с без спецсимволов или больших букв: Переменная - Passnobig
    # Ввод Пароля
    pytest.driver.find_element(By.ID, 'password').send_keys(Passnobig)

    # Ввод потверждения Проля
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(Passnobig)

    # Нажатие Регистрироваться
    pytest.driver.find_element(By.NAME, 'register').click()

    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta.rt-input-container__meta--error')))

    # Проверка на несовпадение паролей
    assert pytest.driver.find_element(By.CLASS_NAME, 'rt-input-container__meta.rt-input-container__meta--error')


# class TestRegistration:
#     """Проверка регистрации на сайте"""
#     # Выносим данные в тело класса для доступа к значениям переменных из всех функций класса:
#     result_email, status_email = RegEmail().get_api_email()  # запрос на получение валидного почтового ящика
#     email_reg = result_email[0]  # из запроса получаем валидный email
#
#     @pytest.mark.reg
#     @pytest.mark.positive
#     def test_get_registration_valid(self, Rostelecom):
#         """Валидный вариант регистрации при использовании email и получения кода для входа на почту.
#          Используем виртуальный почтовый ящик '1secmail.com' и получаем данные через GET запросы.
#          Добавляем созданный email в файл settings."""
#
#         # Нажатие на кнопку регистрация
#         pytest.driver.find_element(By.ID, 'kc-register').click()
#
#         # Ввод Имени
#         pytest.driver.find_element(By.NAME, 'firstName').send_keys(Name)
#
#         # Ввод Фамилий
#         pytest.driver.find_element(By.NAME, 'lastName').send_keys(Familiya)
#
#         # # Ввод Почты
#         # pytest.driver.find_element(By.ID, 'address').send_keys(Mail)
#
#         # Ввод Пароля
#         pytest.driver.find_element(By.ID, 'password').send_keys(Pass)
#
#         # Ввод потверждения Проля
#         pytest.driver.find_element(By.ID, 'password-confirm').send_keys(Pass)
#
#         # Нажатие Регистрироваться
#         pytest.driver.find_element(By.NAME, 'register').click()
#
#         time.sleep(60)
#
#         result_id, status_id = RegEmail().get_id_letter(mail_name, mail_domain)
#         # Получаем id письма с кодом из почтового ящика:
#         id_letter = result_id[0].get('id')
#
#         result_code, status_code = RegEmail().get_reg_code(mail_name, mail_domain, str(id_letter))
#
#         # Получаем body из текста письма:
#         text_body = result_code.get('body')
#         # Извлекаем код из текста методом find:
#         reg_code = text_body[text_body.find('Ваш код : ') + len('Ваш код : '):
#                              text_body.find('Ваш код : ') + len('Ваш код : ') + 6]

def test_registration(Rostelecom):
    # Тест на валидную регистрацию



    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(Name)

    # Ввод Фамилий
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Familiya)

    # Ввод Почты
    pytest.driver.find_element(By.ID, 'address').send_keys(Mail)

    # ВВод пароля с без спецсимволов или больших букв: Переменная - Passnobig
    # Ввод Пароля
    pytest.driver.find_element(By.ID, 'password').send_keys(Pass)

    # Ввод потверждения Проля
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(Pass)

    # Нажатие Регистрироваться
    pytest.driver.find_element(By.NAME, 'register').click()
    time.sleep(20)
    print(Mail)
    time.sleep(5)
    login = Mail.split('@')[0]
    domain = Mail.split('@')[1]
    response = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}')

    messages = response.json()

    meskey = messages[0]['id']
    print(meskey)
    time.sleep(5)

    response = requests.get(
        f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={meskey}')
    text = response.json()
    print(text)
    time.sleep(5)
    soup = BeautifulSoup(text['body'], 'html.parser')
    soupp = soup.p.text.split(': ')[1].strip()
    souppp = list(soupp)
    print(souppp)

    pytest.driver.find_element(By.ID, 'rt-code-0').send_keys(souppp[0])

    pytest.driver.find_element(By.ID, 'rt-code-1').send_keys(souppp[1])

    pytest.driver.find_element(By.ID, 'rt-code-2').send_keys(souppp[2])

    pytest.driver.find_element(By.ID, 'rt-code-3').send_keys(souppp[3])

    pytest.driver.find_element(By.ID, 'rt-code-4').send_keys(souppp[4])

    pytest.driver.find_element(By.ID, 'rt-code-5').send_keys(souppp[5])

