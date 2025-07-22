import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.page_factory import PageFactory


@pytest.fixture
def pages(browser):
    with allure.step('Инициализация страницы'):
        return PageFactory(browser)


@pytest.fixture(scope='function')
def browser():
    with allure.step('Запуск браузера'):
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)

    yield driver
    with allure.step('Закрытие браузера'):
        driver.quit()
