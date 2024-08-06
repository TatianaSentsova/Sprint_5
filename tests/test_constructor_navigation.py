import time

from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import StellarBurgersLocators
from data import Data
from selenium.webdriver.support import expected_conditions as EC


class TestStellarBurgerConstructorNavigation:
    def test_navigation_to_sauces(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_BUTTON).click()

        driver.find_element(*StellarBurgersLocators.USER_EMAIL_FIELD).send_keys(Data.USER_EMAIL)
        driver.find_element(*StellarBurgersLocators.USER_PASSWORD_FIELD).send_keys(Data.USER_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

        driver.find_element(*StellarBurgersLocators.SAUCES_IN_ACTIVE).click()

        # задержка для прокрутки страницы
        time.sleep(1)

        # проверяем, что контент прокручен до нужного раздела
        sauces_location = driver.find_element(*StellarBurgersLocators.SECTION_SAUCES).location
        assert (sauces_location.get('y') < 250) and driver.find_element(*StellarBurgersLocators.SAUCES_ACTIVE)

    def test_navigation_to_fillings(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_BUTTON).click()

        driver.find_element(*StellarBurgersLocators.USER_EMAIL_FIELD).send_keys(Data.USER_EMAIL)
        driver.find_element(*StellarBurgersLocators.USER_PASSWORD_FIELD).send_keys(Data.USER_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

        driver.find_element(*StellarBurgersLocators.FILLINGS_IN_ACTIVE).click()

        # задержка для прокрутки страницы
        time.sleep(1)

        # проверяем, что контент прокручен до нужного раздела
        fillings_location = driver.find_element(*StellarBurgersLocators.SECTION_FILLINGS).location
        assert (fillings_location.get('y') < 250) and driver.find_element(*StellarBurgersLocators.FILLINGS_ACTIVE)

    def test_navigation_to_buns(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_BUTTON).click()

        driver.find_element(*StellarBurgersLocators.USER_EMAIL_FIELD).send_keys(Data.USER_EMAIL)
        driver.find_element(*StellarBurgersLocators.USER_PASSWORD_FIELD).send_keys(Data.USER_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

        driver.find_element(*StellarBurgersLocators.SAUCES_IN_ACTIVE).click()

        # задержка для прокрутки страницы
        time.sleep(1)

        driver.find_element(*StellarBurgersLocators.BUNS_IN_ACTIVE).click()

        # задержка для прокрутки страницы
        time.sleep(1)

        # проверяем, что контент прокручен до нужного раздела
        buns_location = driver.find_element(*StellarBurgersLocators.SECTION_BUNS).location
        assert (buns_location.get('y') < 250) and driver.find_element(*StellarBurgersLocators.BUNS_ACTIVE)
