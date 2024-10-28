from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

users = ['user1@mail.com', 'user2@mail.com', 'user3@mail.com']
passws = ['dsfsdf', 'sdfsdcax', 'asdfsdf']

def generate_pairs():
    pairs = []
    for user in users:
        for passw in passws:
            pairs.append(pytest.param((user, passw), id = f'{user}, {passw}'))
    return pairs


# @pytest.mark.parametrize('creds',
#                          [
#                           pytest.param(('user1@mail.com', 'sdfasdf'), id='user1@mail.com, sdfasdf'),
#                           pytest.param(('user2@mail.com', 'qwiuehdsj'), id='user2@mail.com, qwiuehdsj'),
#                           pytest.param(('user3@mail.com', 'pqwidsncsd'), id='user3@mail.com, pqwidsncsd')
#                          ])


@pytest.mark.skip
@pytest.mark.parametrize('creds', generate_pairs())
def test_login(creds):
    login, passw = creds
    driver = webdriver.Chrome()
    driver.get('https://magento.softwaretestingboard.com/customer/account/login')
    driver.find_element(By.ID, 'email').send_keys(login)
    driver.find_element(By.ID, 'pass').send_keys(passw)
    driver.find_element(By.ID, 'pass').click()
    error_text = driver.find_element(By.CSS_SELECTOR, '[data-ui - id="message-error"]').text


@pytest.fixture()
def page(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    param = request.param
    if param == 'whats_new':
        driver.get('https://magento.softwaretestingboard.com/what-is-new.html')
    elif param == 'sale':
        driver.get('https://magento.softwaretestingboard.com/sale')
    return driver


@pytest.mark.parametrize('page', ['whats_new'], indirect=True)
def test_whats_new(page):
    title = page.find_element(By.CSS_SELECTOR, 'h1')
    assert title.text == 'What\'s New'


@pytest.mark.parametrize('page', ['sale'], indirect=True)
def test_sale(page):
    title = page.find_element(By.CSS_SELECTOR, 'h1')
    assert title.text == 'Sale'
