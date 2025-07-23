import allure

from data.locators.main_page_locators import FooterLocators as loc


@allure.epic('Главная страница')
@allure.feature('Элементы главной страницы')
@allure.story('Проверка контактной информации в футере')
@allure.severity(allure.severity_level.CRITICAL)
def test_footer_contacts_check(open_main_page):
    main_page = open_main_page
    exp_text = main_page.EXPECTED_TEXTS

    with allure.step('1. Проверить отображение адреса.'):
        address_elem = main_page.find_element(loc.ADDRESS)
        assert main_page.get_text(address_elem) == exp_text['address'], \
            'Адрес не соответствует ожидаемому.'

    with (allure.step('2. Проверить наличие номеров телефонов.')):
        phone_3 = main_page.find_element(loc.PHONE1)
        phone_4 = main_page.find_element(loc.PHONE2)
        assert main_page.get_text(phone_3) == exp_text['in_phone3'], \
            'Номер телефона не соответствует ожидаемому.'
        assert main_page.get_text(phone_4) == exp_text['in_phone4'], \
            'Номер телефона не соответствует ожидаемому.'

    with allure.step('3. Проверить отображение адресов email.'):
        email_1 = main_page.find_element(loc.EMAIL1)
        email_2 = main_page.find_element(loc.EMAIL2)
        assert main_page.get_text(email_1) == exp_text['mail'], \
            'Адрес электронной почты не соответствует ожидаемому.'
        assert main_page.get_text(email_2) == exp_text['mail2'], \
            'Адрес электронной почты не соответствует ожидаемому.'
