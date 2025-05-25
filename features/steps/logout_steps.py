# features/steps/logout_steps.py

from behave import when, then
from pages.HomePage import HomePage
from pages.login_page import LoginPage


@then("the user logs out")
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.logout()


