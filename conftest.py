import pytest
from selenium import webdriver
from supportive_data import Urls


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.scooter_url)
    yield driver
    driver.quit()
