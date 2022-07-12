from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.CSS_SELECTOR, '[class="input__control input__input mini-suggest__input"]')
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CSS_SELECTOR, '[class="mini-suggest__button-text"]')
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, "#text")
    LOCATOR_YANDEX_SEARCH_DROPDOWN = (By.CSS_SELECTOR, '[class="mini-suggest__popup-content"]')
    LOCATOR_YANDEX_SEARCH_HREFS = (By.CSS_SELECTOR, '[class="serp-list serp-list_left_yes"]')
    LOCATOR_YANDEX_PICTURE_LINK = (By.CSS_SELECTOR, '[class="services-new__icon services-new__icon_images"]')
    LOCATOR_YANDEX_SEARCH_LINK = (By.CSS_SELECTOR, 'a.Link')
    LOCATOR_YANDEX_PICTURE_FIRST_CATEGORY = (By.CSS_SELECTOR, 'img.PopularRequestList-Thumb')
    LOCATOR_YANDEX_PICTURE_FIRST_CATEGORY_TTT = (By.CSS_SELECTOR, '[data-grid-name="im"]')
    LOCATOR_YANDEX_PICTURE_FIRST_CATEGORY_TTTT = (By.CSS_SELECTOR, '[data-grid-name="im"]')
    LOCATOR_YANDEX_PICTURE_FOR_INPUT_FIELD = (By.CSS_SELECTOR, 'input[name="text"]')
    LOCATOR_YANDEX_OPENED_PICTURE = (By.CSS_SELECTOR, '[class="MMImage-Origin"]')
    LOCATOR_YANDEX_FIRST_CATEGORY_OPEN = (By.CSS_SELECTOR, '.CircleButton_type_next')
    LOCATOR_YANDEX_SECOND_PICTURE = (By.CSS_SELECTOR, '[class="MMImage-Origin"]')
    LOCATOR_YANDEX_THIRD_PICTURE = (By.CSS_SELECTOR, '.CircleButton_type_prev')





class SearchHelper(BasePage):

    def search_element(self, selector):
        element = self.find_elements(selector)
        return element

    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=10).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR, time=10)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def push_keyboard(self, button):
        self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD).send_keys(button)

    def search_href(self, selector):
        return self.find_elements(selector)

    def click_on_the_pictures_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURE_LINK, time=10).click()

    def click_on_the_first_category_pictures(self):
        elements = WebDriverWait(self.driver, 15, 0.3, ignored_exceptions=StaleElementReferenceException)\
            .until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-grid-name="im"]')))
        return elements[0].click(), elements[0].get_attribute('data-grid-text')

    def get_text_by_list_element(self, pos):
        elements = WebDriverWait(self.driver, 15, 0.3, ignored_exceptions=StaleElementReferenceException) \
            .until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-grid-name="im"]')))
        return elements[pos].get_attribute('data-grid-text')

    def text_search_input_field_uniq(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURE_FOR_INPUT_FIELD, time=10)

    def text_search_opened_picture(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_OPENED_PICTURE, time=10)

    def the_first_category(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_FIRST_CATEGORY_OPEN, time=10).click()

    def the_second_picture(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SECOND_PICTURE, time=10)

    def the_third_picture(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_THIRD_PICTURE, time=10).click()

