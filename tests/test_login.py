import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_login(page):

    page.goto("https://app.workflowpro.com/login")

    login = LoginPage(page)

    login.login(
        "admin@company1.com",
        "password123"
    )

    page.wait_for_url("**/dashboard")

    expect(page.locator(".welcome-message")).to_be_visible()
