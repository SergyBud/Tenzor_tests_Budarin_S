import time

from selenium.webdriver import Keys

from yandexsearchPage import SearchHelper, YandexSeacrhLocators


# @pytest.mark.parametrize("word", [("Тензор"), ("Car")])
def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    search_field = yandex_main_page.search_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
    assert search_field, "element not found"
    yandex_main_page.enter_word("Тензор")
    search_dropdown = yandex_main_page.search_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_DROPDOWN)
    assert search_dropdown, "elements not found"
    yandex_main_page.push_keyboard(Keys.ENTER)
    time.sleep(10)
    hrefs = yandex_main_page.search_href(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_HREFS)
    print(hrefs)
    assert 'tensor.ru' in link_pictures, "elements not found"
   # yandex_main_page.click_on_the_search_button()
    #elements = yandex_main_page.check_navigation_bar()
    #assert "Тарифы" in elements

# def test_augh_page(browser):
#    labirint_augh_page = AuthorizationHelper(browser)
#    labirint_augh_page.go_to_site()
#   labirint_augh_page.click_on_the_augh_button_one()
#  labirint_augh_page.enter_code("A16E-43C0-8CC2")
#  labirint_augh_page.click_on_the_augh_button_two()
#  labirint_augh_page.click_on_the_augh_button_three()
#  words = labirint_augh_page.check_page_contain_words()
##  assert "Код скидки A16E-43C0-8CC2" in words
# time.sleep(4)
