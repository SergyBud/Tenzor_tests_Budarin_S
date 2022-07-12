from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        # self.url = url
        self.base_url = "https://yandex.ru/"
        self.wait = WebDriverWait(driver, 15, 0.3, ignored_exceptions=StaleElementReferenceException)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def delete_cookie(self):
        return self.driver.delete_cookie(self.base_url)

