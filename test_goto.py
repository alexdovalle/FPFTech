import re
from playwright.sync_api import Page, expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://automationexercise.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Automation Exercise"))

    page.get_by_role("link", name = "Products").click()

    expect(page).to_have_title(re.compile("All Products"))

    products = page.locator(".productinfo p")
    value = page.locator(".productinfo h2")
    for i in range(products.count()):

        print(products.nth(i).inner_text())
        print(value.nth(i).inner_text())