from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    EXPECTED_TEXTS = {
        'page_title': 'Protractor practice website - Registration',
        'success_text': "You're logged in!!"
    }