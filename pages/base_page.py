# base_page.py
import logging
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from features.configs.config import ENABLE_ALLURE_LOGGING

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)

    def _log_and_allure(self, description, screenshot=False):
        self.logger.info(description)
        if ENABLE_ALLURE_LOGGING:
            with allure.step(description):
                if screenshot:
                    allure.attach(
                        self.driver.get_screenshot_as_png(),
                        name="screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )

    def find_element(self, by, locator):
        try:
            self._log_and_allure(f"Finding element: {by}={locator}")
            return self.wait.until(EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            self._log_and_allure(f"Element not found: {by}={locator}", screenshot=True)
            raise

    def click(self, by, locator):
        try:
            self._log_and_allure(f"Clicking element: {by}={locator}")
            element = self.wait.until(EC.element_to_be_clickable((by, locator)))
            element.click()
        except (TimeoutException, ElementNotInteractableException) as e:
            self._log_and_allure(f"Failed to click element: {by}={locator}", screenshot=True)
            raise e

    def type(self, by, locator, text):
        element = self.find_element(by, locator)
        self._log_and_allure(f"Typing into element: {by}={locator} -> {text}")
        element.clear()
        element.send_keys(text)

    def get_text(self, by, locator):
        element = self.find_element(by, locator)
        text = element.text
        self._log_and_allure(f"Getting text from {by}={locator}: {text}")
        return text

    def is_visible(self, by, locator):
        try:
            self._log_and_allure(f"Checking visibility: {by}={locator}")
            self.wait.until(EC.visibility_of_element_located((by, locator)))
            return True
        except TimeoutException:
            return False

    def get_attribute(self, by, locator, attribute):
        element = self.find_element(by, locator)
        value = element.get_attribute(attribute)
        self._log_and_allure(f"Getting attribute '{attribute}' from {by}={locator}: {value}")
        return value

    def take_screenshot(self, name="screenshot"):
        self._log_and_allure(f"Taking screenshot: {name}", screenshot=True)

    def select_dropdown_by_value(self, by, locator, value):
        from selenium.webdriver.support.ui import Select
        element = self.find_element(by, locator)
        self._log_and_allure(f"Selecting from dropdown {by}={locator} -> {value}")
        Select(element).select_by_value(value)

    def wait_for_element_to_disappear(self, by, locator):
        self._log_and_allure(f"Waiting for element to disappear: {by}={locator}")
        self.wait.until(EC.invisibility_of_element_located((by, locator)))
