import os

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
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        host = "selenoid"
        port = os.getenv("SELENIUM_PORT", "4444")
        command_executor = f"http://{host}:{port}/wd/hub"

        capabilities = {
            "browserName": "chrome",
            "browserVersion": "121.0",
            "selenoid:options": {
                "enableVNC": False,
                "enableVideo": False
            },
            **options.to_capabilities()
        }

        driver = webdriver.Remote(
            command_executor=command_executor,
            # options=options,
            capabilities=capabilities  # type: ignore
        )

    yield driver
    with allure.step('Закрытие браузера'):
        driver.quit()


@pytest.fixture(scope='function')
def open_main_page(pages):
    with allure.step('Открытие главной страницы'):
        pages.main.open(Urls.MAIN_PAGE)
        return pages.main
