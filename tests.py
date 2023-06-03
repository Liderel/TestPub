import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
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
    # Тест на валидную регистрацию

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




