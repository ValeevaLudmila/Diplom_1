import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from data import TestData

@pytest.fixture()
def driver():
    """Фикстура для инициализации и закрытия драйвера."""
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    
    # Установите неявные ожидания
    driver.implicitly_wait(10)
    
    try:
        driver.get(TestData.scooter_address)
        driver.maximize_window()
        yield driver
    finally:
        driver.quit()