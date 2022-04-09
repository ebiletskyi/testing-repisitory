import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('setup')
class TestLoginSite:
    def test_login(self):
        driver = webdriver.Chrome()
        ec = expected_conditions
        wait = WebDriverWait(driver, 1)









