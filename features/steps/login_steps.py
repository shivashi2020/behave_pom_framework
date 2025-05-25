# features/steps/login_steps.py
import os

from behave import given, when, then
from dotenv import load_dotenv

from pages.login_page import LoginPage

@given("I am on the login page")
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    app_url = os.getenv("APP_URL")
    context.driver.get(app_url)


@when('the user logs in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    # from dotenv import load_dotenv
    # load_dotenv()  # ← ADD THIS
    use_env = os.getenv("USE_ENV", "True").lower() == "true"
    if use_env:
        username = os.getenv("LOGIN_USERNAME")
        password = os.getenv("LOGIN_PASSWORD")

    context.login_page.login(username, password)

@then("I should be redirected to the dashboard")
def step_impl(context):
    expected_title = "Demo Web Shop"
    actual_title = context.driver.title
    assert expected_title in actual_title, f"Expected title to contain '{expected_title}', but got '{actual_title}'"