import time

from playwright.sync_api import sync_playwright


with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://demoblaze.com/')

        # click BTN
        page.click("a#login2")

        #Explicit wait
        page.wait_for_selector("div#logInModal", state="visible")

        page.fill('input#loginusername', 'testuser')
        page.fill('input#loginpassword', 'testpass')

        #click login
        page.click("button[onclick='logIn()']")

        page.wait_for_selector("a#logout2",state="visible")
        assert page.is_visible("a#logout2"), "login failed"
        time.sleep(2)

        page.click("a#logout2")
        time.sleep(2)
        browser.close()