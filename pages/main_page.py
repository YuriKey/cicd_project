import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from data.locators.main_page_locators import CarouselLocators as cl
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    EXPECTED_TEXTS = {
        'url_title': 'Get Online Selenium Certification Course | Way2Automation',
        'reg_button_text': 'Register Now',
        'block_courses_title': 'Best Selenium Certification Course Online',
        'life_time_text': 'Lifetime Membership',
        'training_text': 'Online Training',
        'tutorials_text': 'Video Tutorials',
        'corporate_text': 'Corporate Training',
        'facebook_text': 'Facebook',
        'linkedin_text': 'Linkedin',
        'google_plus_text': 'Google',
        'youtube_text': 'Youtube',
        'in_phone1': '+919711-111-558',
        'in_phone2': '+919711-191-558',
        'in_phone3': '+91 97111-11-558',
        'in_phone4': '+91 97111-91-558',
        'us_phone': '+1 646-480-0603',
        'skype_text': 'seleniumcoaching',
        'mail': 'trainer@way2automation.com',
        'mail2': 'seleniumcoaching@gmail.com',
        'address': 'Way2Automation\nCDR Complex, 3rd Floor, Naya Bans Market, Sector 15, Noida, Near sec-16 Metro '
                   'Stationn'
    }

    @staticmethod
    def check_elements_with_text(
            expected_elements: dict[str, tuple[str, str]],
            page: BasePage
    ) -> list[str]:
        with allure.step(f'Проверка элементов навигации на главной странице'):
            missing_elements = []
            for name, locator in expected_elements.items():
                try:
                    expected_text = name
                    actual_text = page.get_text_by_locator(locator)
                    assert actual_text == expected_text, \
                        f'Текст элемента "{name}" некорректен: "{actual_text}" вместо "{expected_text}"'

                except TimeoutException:
                    missing_elements.append(name), f'Возникла проблема с элементом "{name}". Необходима проверка'

        return missing_elements

    @staticmethod
    def check_social_elements(
            expected_elements: dict[str, tuple[str, str]],
            page: BasePage
    ) -> list[str]:
        with allure.step(f'Проверка элементов соцсетей в хедере страницы'):
            missing_elements = []
            for link, locator in expected_elements.items():
                try:
                    soc_element = page.find_element(locator)
                    assert soc_element, f'Элемент "{link}" не отображается на странице'
                    assert soc_element.get_property('href') == link, f'Неверная ссылка для элемента: "{link}"'

                except TimeoutException:
                    missing_elements.append(link), f'Возникла проблема с элементом "{link}". Необходима проверка'
        return missing_elements

    def close_banner(self):
        with allure.step('Закрытие баннера'):
            for _ in range(3):
                try:
                    banner_close = self.wait.until(EC.element_to_be_clickable(cl.BANNER_CLOSE))
                    banner_close.click()
                    self.wait.until(EC.invisibility_of_element_located(cl.BANNER_CLOSE))
                    break
                except:
                    pass

    def get_active_slide_label(self):
        with allure.step('Получение aria-label активного слайда'):
            active_slide = self.find_element(cl.ACTIVE_SLIDE)
            return self.get_attribute_(active_slide, 'aria-label')

    def next_slide(self):
        with allure.step('Переход к следующему слайду'):
            self.click_element_by_js(cl.BTN_RIGHT)
            self.await_for_js_reaction()

    def previous_slide(self):
        with allure.step('Переход к предыдущему слайду'):
            self.click_element_by_js(cl.BTN_LEFT)
            self.await_for_js_reaction()