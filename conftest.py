import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data.urls import Urls
from pages.page_factory import PageFactory


@pytest.fixture
def pages(browser):
    with allure.step('Инициализация страницы'):
        return PageFactory(browser)


@pytest.fixture(scope='function')
def browser():
    with allure.step('Запуск браузера'):
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Remote(
            command_executor=selenium_host,  # need define
            options=chrome_options
        )
        driver.implicitly_wait(10)

    yield driver
    with allure.step('Закрытие браузера'):
        driver.quit()


@pytest.fixture(scope='function')
def open_main_page(pages):
    with allure.step('Открытие главной страницы'):
        pages.main.open(Urls.MAIN_PAGE)
        return pages.main
