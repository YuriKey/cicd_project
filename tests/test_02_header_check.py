import allure

from data.locators.main_page_locators import HeaderLocators as loc


@allure.epic('Главная страница')
@allure.feature('Элементы страницы')
@allure.story('Проверка контактной информации в хедере')
@allure.severity(allure.severity_level.CRITICAL)
def test_header_contacts_check(open_main_page):
    main_page = open_main_page
    exp_text = main_page.EXPECTED_TEXTS

    with allure.step('1. Проверка наличия номеров телефонов в хедере'):
        in_phone1 = main_page.find_element(loc.PHONE1_INDIAN)
        in_phone2 = main_page.find_element(loc.PHONE2_INDIAN)
        us_phone = main_page.find_element(loc.PHONE_US)
        assert in_phone1 and main_page.get_text(in_phone1) == exp_text['in_phone1'], \
            f'Неверный текст номера телефона {exp_text['in_phone1']}'
        assert in_phone2 and main_page.get_text(in_phone2) == exp_text['in_phone2'], \
            f'Неверный текст номера телефона {exp_text['in_phone2']}'
        assert us_phone and main_page.get_text(us_phone) == exp_text['us_phone'], \
            f'Неверный текст номера телефона {exp_text['us_phone']}'

    with allure.step('2. Проверка наличия ссылки на скайп в хедере'):
        skype = main_page.find_element(loc.SKYPE_LINK)
        assert skype and main_page.get_text(skype) == exp_text['skype_text'], \
            f'Неверный текст ссылки на скайп {exp_text['skype_text']}'

    with allure.step('3. Проверка наличия ссылки на почту в хедере'):
        email = main_page.find_element(loc.EMAIL_LINK)
        assert email and main_page.get_text(email) == exp_text['mail'], \
            f'Неверный текст ссылки на почту {exp_text['mail']}'

    with allure.step('4. Проверка наличия ссылок на соцсети в хедере'):
        social_elements = loc.SOCIAL_ELEMENTS
        missing_elements = main_page.check_social_elements(social_elements, main_page)

        assert not missing_elements, (f'Отсутствуют следующие элементы соц.сетей:'
                                      f' {', '.join(missing_elements)}')