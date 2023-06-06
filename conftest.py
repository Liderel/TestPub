import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
#
#
@pytest.fixture(autouse=True)
def Rostelecom():
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    pytest.driver.get('https://b2c.passport.rt.ru/')
    # Устанавливаем пользовательское разрешение экрана
    pytest.driver.set_window_size(1920, 1080)

    wait = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'app-header')))

    yield
    #
    # pytest.driver.quit()
# #
# # @pytest.fixture(autouse=True)
# def EMail():
#     proverka01()
#     driver = webdriver.Chrome('chromedriver.exe')
#     driver.get('https://www.1secmail.com//')
#     # Устанавливаем пользовательское разрешение экрана
#     driver.set_window_size(1920, 1080)
#
#     driver.execute_script("window.open('https://b2c.passport.rt.ru/')")
#     # driver.switch_to_window(driver.window_handles[0])
#     # driver.switch_to_window(driver.window_handles[1])
#     # driver.switch_to_window(driver.window_handles[0])
#     #
#     # llogin = driver.find_element(By.ID, 'login').get_attribute('value')
#     # print(llogin)
#     # domain = Select(driver.find_element(By.ID, 'domain'))
#     # o = domain.first_selected_option
#     # print(o.text)
#     #
#     # eemail = f"{llogin}{o.text}"
#     # print(eemail)
#     #
#     # wait = WebDriverWait(pytest.driver, 10).until(
#     # #     EC.presence_of_element_located((By.ID, 'logo')))
#     #
#     #
#     # yield
#     #
#     # pytest.driver.quit()
#
# def proverka01():
#     print('Hello')
#
# EMail()