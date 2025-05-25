# drivers/browser.py
from selenium import webdriver

def get_driver(browser_name):
    if browser_name.lower() == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(options=options)
    raise Exception(f"{browser_name} is not supported.")
