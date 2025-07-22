from selenium.webdriver.common.by import By


class NavigationLocators:
    NAVI_HOME_BUTTON = (By.XPATH, '//*[@id="menu-item-27578"]')
    NAVI_ALL_COURSES_BUTTON = (By.XPATH, '//*[@id="menu-item-27580"]')
    NAVI_VIDEO_TUTORIAL_BUTTON = (By.XPATH, '//*[@id="menu-item-27597"]')
    NAVI_RESOURCES_BUTTON = (By.XPATH, '//*[@id="menu-item-27617"]')
    NAVI_CAREERS_BUTTON = (By.XPATH, '//*[@id="menu-item-27621"]')
    NAVI_LIFETIME_MEMBERSHIP_BUTTON = (By.XPATH, '//*[@id="menu-item-27622"]')
    NAVI_BLOG_BUTTON = (By.XPATH, '//*[@id="menu-item-27623"]')
    NAVI_FORUM_BUTTON = (By.XPATH, '//*[@id="menu-item-27624"]')
    NAVI_MEMBER_LOGIN_BUTTON = (By.XPATH, '//*[@id="menu-item-27625"]')
    REGISTER_BUTTON = (By.XPATH, '//*[@class="elementor-button elementor-slide-button elementor-size-sm"][contains('
                                 'text(), "Register Now")]')
    COURSES_BLOCK_CONTAINER = (By.XPATH, '//h1[text()]/ancestor::div[contains(@class, "elementor-widget-wrap")]')
    LIFETIME_MENU_ITEM = (By.ID, 'menu-item-27581')

    NAVIGATION_ELEMENTS = {
        'Home': NAVI_HOME_BUTTON,
        'All Courses': NAVI_ALL_COURSES_BUTTON,
        'Video Tutorial': NAVI_VIDEO_TUTORIAL_BUTTON,
        'Resources': NAVI_RESOURCES_BUTTON,
        'Careers': NAVI_CAREERS_BUTTON,
        'Lifetime Membership': NAVI_LIFETIME_MEMBERSHIP_BUTTON,
        'Blog': NAVI_BLOG_BUTTON,
        'Forum': NAVI_FORUM_BUTTON,
        'Member Login': NAVI_MEMBER_LOGIN_BUTTON
    }


class HeaderLocators:
    HEADER = (By.XPATH, '//*[contains(@class, "main-header-bar site-header-focus-item")]')
    PHONE1_INDIAN = (By.XPATH, '//*[@class="elementor-icon-list-text"][contains(text(), "+919711-111-558")]')
    PHONE2_INDIAN = (By.XPATH, '//*[@class="elementor-icon-list-text"][contains(text(), "+919711-191-558")]')
    PHONE_US = (By.XPATH, '//*[@class="elementor-icon-list-text"][contains(text(), "+1 646-480-0603")]')
    SKYPE_LINK = (By.XPATH, '//*[@class="elementor-icon-list-text"][normalize-space(text()) = "seleniumcoaching"]')
    EMAIL_LINK = (By.XPATH,
                  '//*[@class="elementor-icon-list-text"][contains(text(), "trainer@way2automation.com")]['
                  'ancestor::li[contains(@class, "elementor-icon-list-item") and contains(@class, '
                  '"elementor-inline-item")]]')
    FACEBOOK_ICON = (By.XPATH, '//a[@aria-label="Facebook"]')
    LINKEDIN_ICON = (By.XPATH, '//a[@aria-label="Linkedin"]')
    GOOGLEPLUS_ICON = (By.XPATH, '//a[@aria-label="Google"]')
    YOUTUBE_ICON = (By.XPATH, '//a[@aria-label="YouTube"]')

    SOCIAL_ELEMENTS = {
        'https://www.facebook.com/way2automation': FACEBOOK_ICON,
        'https://in.linkedin.com/in/rahul-arora-0490b751': LINKEDIN_ICON,
        'https://plus.google.com/u/0/+RamanAhujatheseleniumguru': GOOGLEPLUS_ICON,
        'https://www.youtube.com/c/seleniumappiumtutorialtraining': YOUTUBE_ICON
    }


class FooterLocators:
    FOOTER = (By.ID, 'colophon')
    ADDRESS = (By.XPATH, '//*[@class="elementor-icon-list-text"][contains(text(), "Way2Automation")]')
    PHONE1 = (By.XPATH, '//*[@class="elementor-icon-list-text"][contains(text(), "+91 97111-11-558")]')
    PHONE2 = (By.XPATH, '//*[@class="elementor-icon-list-text"][contains(text(), "+91 97111-91-558")]')
    EMAIL1 = (By.XPATH, '//*[@class="elementor-icon-list-text"]'
                        '[contains(text(), "trainer@way2automation.com")]'
                        '[not(ancestor::li[contains(@class, "elementor-inline-item")])]')

    EMAIL2 = (By.XPATH, '//*[@class="elementor-icon-list-text"][contains(text(), "seleniumcoaching@gmail.com")]')


class CarouselLocators:
    COURSES_BLOCK = (By.CSS_SELECTOR, '.pp-info-box-carousel-wrap.swiper-container-wrap')
    BTN_RIGHT = (By.XPATH, '//div[@class="pp-slider-arrow swiper-button-next swiper-button-next-c50f9f0"]')
    BTN_LEFT = (By.XPATH, '//div[@class="pp-slider-arrow swiper-button-prev swiper-button-prev-c50f9f0"]')
    BANNER_CLOSE = (By.XPATH, '//*[@aria-label="Close"]')
    ACTIVE_SLIDE = (By.XPATH, '//*[@class="swiper-slide swiper-slide-active"][contains(@aria-label, "/ 16")]')