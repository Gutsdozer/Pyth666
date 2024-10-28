from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest



@pytest.fixture()
def driver():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(5)
    chrome_browser.maximize_window()
    return chrome_browser

def test_message(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    message = driver.find_element(By.XPATH, '//*[text() = "Default welcome msg"]')
    assert message.is_displayed()


def test_add_to_cart(driver):
    driver.get('https://magento.softwaretestingboard.com/proteus-fitness-jackshirt.html')
    driver.find_element(By.ID, 'option-label-size-143-item-166').click()
    driver.find_element(By.ID, 'option-label-color-93-item-49').click()
    driver.find_element(By.ID, 'product-addtocart-button').click()