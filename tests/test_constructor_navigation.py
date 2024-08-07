from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import StellarBurgersLocators
from selenium.webdriver.support import expected_conditions as EC


class TestStellarBurgerConstructorNavigation:
    def test_navigation_to_sauces(self, driver):
        driver.find_element(*StellarBurgersLocators.SAUCES_BUTTON_INACTIVE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.SAUCES_SECTION))
        sauces_section = driver.find_element(*StellarBurgersLocators.SAUCES_SECTION)
        sauces_button_active = driver.find_element(*StellarBurgersLocators.SAUCES_BUTTON_ACTIVE)
        assert sauces_section.is_displayed() and sauces_button_active.is_displayed()

    def test_navigation_to_fillings(self, driver):
        driver.find_element(*StellarBurgersLocators.FILLINGS_BUTTON_INACTIVE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.FILLINGS_SECTION))
        fillings_section = driver.find_element(*StellarBurgersLocators.FILLINGS_SECTION)
        fillings_button_active = driver.find_element(*StellarBurgersLocators.FILLINGS_BUTTON_ACTIVE)
        assert fillings_section.is_displayed() and fillings_button_active.is_displayed()

    def test_navigation_to_buns(self, driver):
        driver.find_element(*StellarBurgersLocators.SAUCES_BUTTON_INACTIVE).click()
        driver.find_element(*StellarBurgersLocators.BUNS_BUTTON_INACTIVE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.BUNS_SECTION))
        buns_section = driver.find_element(*StellarBurgersLocators.BUNS_SECTION)
        buns_button_active = driver.find_element(*StellarBurgersLocators.BUNS_BUTTON_ACTIVE)
        assert buns_section.is_displayed() and buns_button_active.is_displayed()
