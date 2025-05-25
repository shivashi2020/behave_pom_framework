from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    LOGOUT_LINK = (By.LINK_TEXT, "Log out")  # or use By.XPATH if needed

    def logout(self):
        self._log_and_allure("Clicking logout link")
        self.click(*self.LOGOUT_LINK)