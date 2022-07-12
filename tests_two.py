from yandexsearchPage import SearchHelper, YandexSeacrhLocators

def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    pictures_link = yandex_main_page.search_element(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURE_LINK)
    assert pictures_link, "element not found"
    yandex_main_page.click_on_the_pictures_button()
    browser.switch_to.window(browser.window_handles[1])
    link_pictures = browser.current_url
    assert 'https://yandex.ru/images' in link_pictures, "elements not found"

    text_catagory = yandex_main_page.get_text_by_list_element(0)
    yandex_main_page.click_on_the_first_category_pictures()
    text_search_input_field = yandex_main_page.text_search_input_field_uniq().get_attribute('value')
    assert text_catagory == text_search_input_field, f"don`t equal, cuz {text_catagory}, {text_search_input_field}"
    pictures_by_category = browser.find_elements_by_css_selector('[class="serp-item__thumb justifier__thumb"]')
    pictures_by_category[0].click()
    opened_picture = yandex_main_page.text_search_opened_picture()
    src_opened_picture = opened_picture.get_attribute('src')
    assert opened_picture, 'picture don`t open'
    yandex_main_page.the_first_category()
    opened_picture_the_second = yandex_main_page.the_second_picture()
    src_opened_picture_the_second = opened_picture_the_second.get_attribute('src')
    assert src_opened_picture != src_opened_picture_the_second
    yandex_main_page.the_third_picture()
    opened_picture_the_third = yandex_main_page.the_second_picture()
    src_opened_picture_the_third = opened_picture_the_third.get_attribute('src')
    assert src_opened_picture == src_opened_picture_the_third


