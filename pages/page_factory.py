from pages.base_page import BasePage
from pages.home_page import HomePage
# from pages.lifetime_page import LifetimePage
# from pages.login_page import LoginPage
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

    # @property
    # def login(self) -> LoginPage:
    #     if 'login' not in self._cache:
    #         self._cache['login'] = LoginPage(self.driver)
    #     return self._cache['login']

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

    # @property
    # def lifetime(self) -> LifetimePage:
    #     if 'lifetime' not in self._cache:
    #         self._cache['lifetime'] = LifetimePage(self.driver)
    #     return self._cache['lifetime']
