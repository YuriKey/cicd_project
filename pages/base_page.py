import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def find_element(self, locator: tuple[str, str]) -> object:
        with allure.step(f'Поиск элемента по локатору {locator}'):
            return self.wait.until(EC.visibility_of_element_located(locator))

    def open(self, url: str) -> None:
        with allure.step('Открытие страницы по URL'):
            self.browser.get(url)

    def click_element(self, locator: tuple[str, str]) -> None:
        with allure.step(f'Клик по элементу с локатором: {locator}'):
            self.wait.until(
                EC.element_to_be_clickable(locator),
                message=f'Не удалось найти кликабельный элемент с локатором {locator}'
            ).click()

    def click_element_by_js(self, element: object) -> None:
        with allure.step('Клик по элементу с помощью JS'):
            try:
                self.browser.execute_script("""
                    var elem = arguments[0];
                    var event = new MouseEvent('click', {
                        bubbles: true,
                        cancelable: true,
                        view: window
                    });
                    elem.dispatchEvent(event);
                """, element)
            except Exception as e:
                raise Exception(f'Не удалось выполнить JS-клик: {str(e)}')

    def fill_field(self, locator: tuple[str, str], text: str) -> None:
        with allure.step('Заполнение поля'):
            self.find_element(locator).send_keys(text)

    def is_element_visible(self, locator: tuple[str, str]) -> bool:
        with allure.step('Проверка видимости элемента'):
            try:
                self.find_element(locator).is_displayed()
                return True
            except TimeoutException:
                return False

    def is_element_clickable(self, locator: tuple[str, str]) -> bool:
        with allure.step('Проверка кликабельности элемента'):
            try:
                self.wait.until(EC.element_to_be_clickable(locator))
                return True
            except TimeoutException:
                return False

    def is_element_invisible(self, locator: tuple[str, str]) -> bool:
        with allure.step('Проверка невидимости элемента'):
            try:
                self.wait.until(EC.invisibility_of_element_located(locator))
                return True
            except TimeoutException:
                return False

    def get_text_by_locator(self, locator: tuple[str, str]) -> str:
        with allure.step('Получение текста из элемента по локатору'):
            return self.find_element(locator).text

    @staticmethod
    def get_text(element: object) -> str:
        with allure.step('Получение текста из элемента по объекту'):
            return element.text

    @staticmethod
    def get_attribute_(element: object, attribute_name: str) -> str:
        with allure.step('Получение значения атрибута по объекту и имени атрибута'):
            return element.get_attribute(attribute_name)

    @staticmethod
    def get_prop_value(element: object, property_name: str) -> str:
        with allure.step('Получение значения свойства по объекту и имени свойства'):
            return element.value_of_css_property(property_name)

    def get_title(self) -> str:
        with allure.step('Получение заголовка страницы'):
            return self.browser.title

    def get_current_url(self) -> str:
        with allure.step('Получение URL текущей страницы'):
            return self.browser.current_url

    def scroll_to_element(self, locator: tuple[str, str]) -> None:
        with allure.step('Скроллинг до элемента'):
            try:
                element = self.find_element(locator)
                self.browser.execute_script('arguments[0].scrollIntoView({behavior: "auto", block: "center"});',
                                            element)

            except Exception as e:
                print(f'Ошибка при скроллинге до элемента: {e}')

    def scroll_to_bottom(self) -> None:
        with allure.step('Скроллинг до конца страницы'):
            last_height = self.browser.execute_script('return document.body.scrollHeight')
            while True:
                self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                self.await_for_js_reaction()
                new_height = self.browser.execute_script('return document.body.scrollHeight')
                if new_height == last_height:
                    break
                last_height = new_height

    @staticmethod
    def await_for_js_reaction() -> None:
        time.sleep(1)