from selectors import SelectSelector

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.close()



def test_open_s6(browser):
    browser.get('https://demoblaze.com/index.html')
    browser.implicitly_wait(5)

    galaxy_s6 = browser.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
    galaxy_s6.click()
    title = browser.find_element(By.CSS_SELECTOR, 'h2')
    assert  title.text == 'Samsung galaxy s6'


def test_two_monitors(browser):
    browser.get('https://demoblaze.com/index.html')
    monitor_link = browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    monitor_link.click()
    monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
    assert len(monitors) == 2




