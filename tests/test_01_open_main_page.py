import allure
from data.locators.main_page_locators import NavigationLocators as loc
from data.urls import Urls

urls = Urls()


@allure.epic('Главная страница')
@allure.feature('Элементы страницы')
@allure.story('Проверка открытия страницы')
@allure.severity(allure.severity_level.BLOCKER)
def test_main_page_open(pages):
    main_page = pages.main
    main_page.open(urls.MAIN_PAGE)
    exp_text = main_page.EXPECTED_TEXTS

    with allure.step('1. Проверка текущего URL и заголовка страницы'):
        assert main_page.get_current_url() == urls.MAIN_PAGE, 'Неверный URL главной страницы'
        assert main_page.get_title() == exp_text['url_title'], 'Неверный заголовок страницы'

    with allure.step('2. Проверка наличия и текста кнопок в блоке навигации'):
        navigation_elements = loc.NAVIGATION_ELEMENTS
        missing_elements = main_page.check_elements_with_text(navigation_elements, main_page)

        assert not missing_elements, (f'Отсутствуют следующие элементы навигации: {", ".join(missing_elements)}')

    with allure.step('3. Проверка наличия и текста кнопки регистрации'):
        reg_button = main_page.find_element(loc.REGISTER_BUTTON)

        assert reg_button, 'Кнопка регистрация отсутствует'
        assert main_page.get_text(reg_button) == exp_text['reg_button_text'], \
            'Неверный текст для кнопки "Register Now"'

    with allure.step('4. Проверка наличия и текста блока курсов'):
        block_element = main_page.find_element(loc.COURSES_BLOCK_CONTAINER)
        block_text = main_page.get_text(block_element)

        assert exp_text['block_courses_title'] in block_text, 'Блок курсов не содержит заголовок'
        assert exp_text['life_time_text'] in block_text, 'Блок курсов не содержит Lifetime Membership'
        assert exp_text['training_text'] in block_text, 'Блок курсов не содержит Online Training'
        assert exp_text['tutorials_text'] in block_text, 'Блок курсов не содержит Video Tutorials'
        assert exp_text['corporate_text'] in block_text, 'Блок курсов не содержит Corporate Training'
