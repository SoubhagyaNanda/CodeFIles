from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Ued to connect with the browser.
    browser = p.chromium.launch(headless=False)

    # Opening a new context or page
    context = browser.new_context()

    # This will open a new page
    page = context.new_page()

    # This is used for navigation
    page.goto('')

    browser.close()