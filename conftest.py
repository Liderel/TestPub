import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def Rostelecom():
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    pytest.driver.get('https://b2c.passport.rt.ru/')
    # Устанавливаем пользовательское разрешение экрана
    pytest.driver.set_window_size(1920, 1080)

    wait = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'app-header')))

    yield

    pytest.driver.quit()