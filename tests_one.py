from selenium.webdriver import Keys
from yandexsearchPage import SearchHelper, YandexSeacrhLocators
import time

def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    search_field = yandex_main_page.search_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
    assert search_field, "element not found"
    yandex_main_page.enter_word("Тензор")
    search_dropdown = yandex_main_page.search_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_DROPDOWN)
    assert search_dropdown, "elements not found"
    yandex_main_page.push_keyboard(Keys.ENTER)
    search_link_href = yandex_main_page.search_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_LINK)[0].get_attribute("href")
    assert 'tensor.ru' in search_link_href, "elements not found"
