# features/environment.py
import allure
from dotenv import load_dotenv
import logging
from drivers.browser import get_driver
from features.configs.config import BROWSER

def before_all(context):

    load_dotenv()  # Load environment variables from .env file

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

def before_scenario(context, scenario):
    context.driver = get_driver(BROWSER)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        screenshot_path = f"reports/{scenario.name}.png"
        context.driver.save_screenshot(screenshot_path)

        # Attach screenshot file to Allure report
        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name="screenshot", attachment_type=allure.attachment_type.PNG)

    if not context.config.userdata.get("keep_browser", False):
        context.driver.quit()

