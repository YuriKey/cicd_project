import allure
import pytest

from selenium import webdriver
from selenium.webdriver import Remote
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
        chrome_options.set_capability("browserName", "chrome")
        chrome_options.set_capability("browserVersion", "120.0")
        chrome_options.set_capability("selenoid:options", {
            "enableVNC": False,
            "enableVideo": False,
            "enableLog": True
        })
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-setuid-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.binary_location = '/usr/bin/google-chrome'
        chrome_options.add_argument("--remote-debugging-port=9230")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')

        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Remote(
            command_executor='http://selenoid:4445/wd/hub',
            options=chrome_options
        )
        driver.implicitly_wait(10)

        yield driver
        with allure.step('Закрытие браузера'):
            driver.stop_client()
        driver.close()
        driver.quit()
