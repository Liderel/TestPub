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

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, 'rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Пароли не совпадают'

def test_Incorrect_nametoshort_registration(Rostelecom):
    # Тест на не правильное потверждение пароля при регистрации

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys('Т')

    pytest.driver.find_element(By.NAME, 'register').click()

    # Проверка на ошибку что имя слишком короткое
    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

def test_Incorrect_nametolong_registration(Rostelecom):
    # Тест на не правильное потверждение пароля при регистрации

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys('Тесттесттетстетстесттесттетстест')

    pytest.driver.find_element(By.ID, 'password').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR,
                                            '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

def test_Incorrect_namelatin_registration(Rostelecom):
    # Тест на не правильное потверждение пароля при регистрации

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'firstName').send_keys('Test')

    pytest.driver.find_element(By.ID, 'password').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR,
                                            '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

def test_Incorrect_familiyashort_registration(Rostelecom):
    # Тест на не правильное потверждение пароля при регистрации

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'lastName').send_keys('Т')

    pytest.driver.find_element(By.ID, 'password').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR,
                                            '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

def test_Incorrect_familiyatolong_registration(Rostelecom):
    # Тест на не правильное потверждение пароля при регистрации

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'lastName').send_keys('Тесттесттетстетстесттесттетстест')

    pytest.driver.find_element(By.ID, 'password').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR,
                                            '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


def test_Incorrect_familiyalatin_registration(Rostelecom):
    # Тест на не правильное потверждение пароля при регистрации

    # Нажатие на кнопку регистрация
    pytest.driver.find_element(By.ID, 'kc-register').click()

    # Ввод Имени
    pytest.driver.find_element(By.NAME, 'lastName').send_keys('Test')

    pytest.driver.find_element(By.ID, 'password').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR,
                                            '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


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

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Пароль должен содержать только латинские буквы'


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

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Пароль должен содержать хотя бы одну заглавную букву'

def test_short_registration(Rostelecom):
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
    pytest.driver.find_element(By.ID, 'password').send_keys('Test001')

    # Ввод потверждения Проля
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('Test001')

    # Нажатие Регистрироваться
    pytest.driver.find_element(By.NAME, 'register').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Длина пароля должна быть не менее 8 символов'

def test_nonumbers_registration(Rostelecom):
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
    pytest.driver.find_element(By.ID, 'password').send_keys('Testtest')

    # Ввод потверждения Проля
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('Testtest')

    # Нажатие Регистрироваться
    pytest.driver.find_element(By.NAME, 'register').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'

def test_tolong_registration(Rostelecom):
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
    pytest.driver.find_element(By.ID, 'password').send_keys('Testtesttesttesttest1')

    # Ввод потверждения Проля
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('Testtesttesttesttest1')

    # Нажатие Регистрироваться
    pytest.driver.find_element(By.NAME, 'register').click()

    error_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error')

    assert error_mess.text == 'Длина пароля должна быть не более 20 символов'