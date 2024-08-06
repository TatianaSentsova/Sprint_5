from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import StellarBurgersLocators
from data import Data
from selenium.webdriver.support import expected_conditions as EC


class TestStellarBurgerLogOut:
    def test_log_out(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_BUTTON).click()

        driver.find_element(*StellarBurgersLocators.USER_EMAIL_FIELD).send_keys(Data.USER_EMAIL)
        driver.find_element(*StellarBurgersLocators.USER_PASSWORD_FIELD).send_keys(Data.USER_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.PROFILE_INFORMATION))

        driver.find_element(*StellarBurgersLocators.LOG_OUT_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.LOGIN_BUTTON))
