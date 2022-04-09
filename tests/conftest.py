import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def get_chrome_options():
    options = Options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://auth.viyar.ua/auth/realms/ViyarAuth/protocol/openid-connect/auth?state=95a59bedb9526e343d16086b62de69d2&scope=profile%20email&response_type=code&approval_prompt=auto&redirect_uri=https%3A%2F%2Fviyar.ua%2Fauth_check&client_id=viyarsites'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()


