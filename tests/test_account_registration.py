from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import StellarBurgersLocators
from data import Data
from selenium.webdriver.support import expected_conditions as EC


class TestStellarBurgerRegistration:
    def test_account_registration(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_BUTTON).click()

        driver.find_element(*StellarBurgersLocators.SIGN_UP_LINK).click()

        driver.find_element(*StellarBurgersLocators.USER_NAME_FIELD).send_keys(Data.NAME)
        driver.find_element(*StellarBurgersLocators.USER_EMAIL_FIELD).send_keys(Data.EMAIL)
        driver.find_element(*StellarBurgersLocators.USER_PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.LOGIN_BUTTON))

        driver.find_element(*StellarBurgersLocators.USER_EMAIL_FIELD).send_keys(Data.EMAIL)
        driver.find_element(*StellarBurgersLocators.USER_PASSWORD_FIELD).send_keys(Data.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

    def test_account_registration_invalid_password(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.SIGN_UP_LINK).click()

        driver.find_element(*StellarBurgersLocators.USER_NAME_FIELD).send_keys(Data.NAME)
        driver.find_element(*StellarBurgersLocators.USER_EMAIL_FIELD).send_keys(Data.EMAIL)
        driver.find_element(*StellarBurgersLocators.USER_PASSWORD_FIELD).send_keys(Data.INVALID_PASSWORD)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()

        error_message = driver.find_element(*StellarBurgersLocators.INVALID_PASSWORD_MESSAGE).text
        assert error_message == 'Некорректный пароль'
