import pytest
from selenium import webdriver
from testdata import ApplicationData


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1470, 730)
    driver.get(ApplicationData.STELLAR_BURGERS_URL)

    yield driver

    driver.quit()
