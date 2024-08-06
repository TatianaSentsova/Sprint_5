from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import StellarBurgersLocators
from data import Data
from selenium.webdriver.support import expected_conditions as EC


class TestStellarBurgerAuthorization:
    def test_login_with_sign_in_button(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_BUTTON).click()

        driver.find_element(*StellarBurgersLocators.USER_EMAIL_FIELD).send_keys(Data.USER_EMAIL)
        driver.find_element(*StellarBurgersLocators.USER_PASSWORD_FIELD).send_keys(Data.USER_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

    def test_login_with_personal_account_button(self, driver):
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()

        driver.find_element(*StellarBurgersLocators.USER_EMAIL_FIELD).send_keys(Data.USER_EMAIL)
        driver.find_element(*StellarBurgersLocators.USER_PASSWORD_FIELD).send_keys(Data.USER_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

    def test_login_with_sign_in_link_on_registration_page(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_BUTTON).click()

        driver.find_element(*StellarBurgersLocators.SIGN_UP_LINK).click()

        driver.find_element(*StellarBurgersLocators.SIGN_IN_LINK).click()

        driver.find_element(*StellarBurgersLocators.USER_EMAIL_FIELD).send_keys(Data.USER_EMAIL)
        driver.find_element(*StellarBurgersLocators.USER_PASSWORD_FIELD).send_keys(Data.USER_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

    def test_login_with_restore_password(self,driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_BUTTON).click()

        driver.find_element(*StellarBurgersLocators.RESTORE_PASSWORD_LINK).click()

        driver.find_element(*StellarBurgersLocators.SIGN_IN_LINK).click()

        driver.find_element(*StellarBurgersLocators.USER_EMAIL_FIELD).send_keys(Data.USER_EMAIL)
        driver.find_element(*StellarBurgersLocators.USER_PASSWORD_FIELD).send_keys(Data.USER_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
