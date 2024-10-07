import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser



def test_open_s6(browser):
    browser.get("https://demoblaze.com/index.html")
    galaxy_s6 = browser.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
    galaxy_s6.click()

