import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
