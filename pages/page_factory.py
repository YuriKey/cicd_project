from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.main_page import MainPage


class PageFactory:
    def __init__(self, driver):
        self.driver = driver
        self._cache = {}

    @property
    def base(self) -> BasePage:
        if 'base' not in self._cache:
            self._cache['base'] = BasePage(self.driver)
        return self._cache['base']

    @property
    def main(self) -> MainPage:
        if 'main' not in self._cache:
            self._cache['main'] = MainPage(self.driver)
        return self._cache['main']

    @property
    def home(self) -> HomePage:
        if 'home' not in self._cache:
            self._cache['main'] = HomePage(self.driver)
        return self._cache['main']
