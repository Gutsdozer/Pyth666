from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(5)
    return chrome_driver


def test_jackets(driver):
    driver.get("https://magento.softwaretestingboard.com/")
    women = driver.find_element(By.ID, "ui-id-4")
    tops = driver.find_element(By.ID, "ui-id-9")
    jackets = driver.find_element(By.ID, "ui-id-11")
    #ActionChains(driver).move_to_element(women).move_to_element(tops).move_to_element(jackets).perform()
    actions = ActionChains(driver)
    actions.move_to_element(women)
    actions.move_to_element(tops)
    actions.move_to_element(jackets)
    actions.perform()


def test_dnd(driver):
    driver.get("https://www.qa-practice.com/elements/dragndrop/boxes")
    drag_me = driver.find_element(By.ID, 'rect-draggable')
    drag_here = driver.find_element(By.ID, 'rect-droppable')
    ActionChains(driver).drag_and_drop(drag_me, drag_here).perform()


def test_open_tab(driver):
    driver.get("https://www.qa-practice.com/elements/dragndrop/boxes")
    inputs = driver.find_element(By.LINK_TEXT, 'Inputs')
    ActionChains(driver).key_down(Keys.CONTROL).click(inputs).key_up(Keys.CONTROL).perform()