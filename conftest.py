import os

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data.urls import Urls
from pages.page_factory import PageFactory


selenium_host = os.getenv("SELENIUM_HOST", "http://selenoid:4444/wd/hub")


@pytest.fixture
def pages(browser):
    with allure.step('Инициализация страницы'):
        return PageFactory(browser)


@pytest.fixture(scope='function')
def browser():
    logger.info(f"Connecting to Selenoid at: {selenium_host}")
    with allure.step('Запуск браузера'):
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        try:
            driver = webdriver.Remote(
                command_executor=selenium_host,
                options=chrome_options
            )
            logger.info("Browser session created successfully")
        except Exception as e:
            logger.error(f"Failed to create browser session: {str(e)}")
            raise
        driver.implicitly_wait(10)

    yield driver
    with allure.step('Закрытие браузера'):
        driver.quit()


@pytest.fixture(scope='function')
def open_main_page(pages):
    with allure.step('Открытие главной страницы'):
        pages.main.open(Urls.MAIN_PAGE)
        return pages.main
