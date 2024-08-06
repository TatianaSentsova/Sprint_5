import pytest
from selenium import webdriver
from data import Data


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1470, 730)
    driver.get(Data.STELLAR_BURGERS_URL)

    yield driver

    driver.quit()
