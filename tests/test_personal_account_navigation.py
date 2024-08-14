from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import StellarBurgersLocators
from testdata import TestData
from selenium.webdriver.support import expected_conditions as EC


class TestStellarBurgerPersonalAccountNavigation:
    def test_navigation_to_personal_account(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.USER_EMAIL_FIELD).send_keys(TestData.USER_EMAIL)
        driver.find_element(*StellarBurgersLocators.USER_PASSWORD_FIELD).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.PROFILE_INFORMATION))
        assert driver.find_element(*StellarBurgersLocators.PROFILE_INFORMATION).is_displayed()

    def test_navigation_to_constructor(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.USER_EMAIL_FIELD).send_keys(TestData.USER_EMAIL)
        driver.find_element(*StellarBurgersLocators.USER_PASSWORD_FIELD).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.PROFILE_INFORMATION))
        driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        assert driver.find_element(*StellarBurgersLocators.MAKE_BURGER).is_displayed()

    def test_navigation_to_logo(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.USER_EMAIL_FIELD).send_keys(TestData.USER_EMAIL)
        driver.find_element(*StellarBurgersLocators.USER_PASSWORD_FIELD).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.PROFILE_INFORMATION))
        driver.find_element(*StellarBurgersLocators.LOGO).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        assert driver.find_element(*StellarBurgersLocators.MAKE_BURGER).is_displayed()
