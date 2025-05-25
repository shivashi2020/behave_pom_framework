# pages/login_page.py
from selenium.webdriver.common.by import By
from  pages.base_page import BasePage


class LoginPage(BasePage):

    SIGNIN = (By.XPATH , "//a[text()='Log in']")
    USERNAME = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BTN = (By.XPATH, "//input[@value='Log in']")

    def login(self, username, password):
        self.click(*self.SIGNIN)
        self.type(*self.USERNAME, username)
        self.type(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)
