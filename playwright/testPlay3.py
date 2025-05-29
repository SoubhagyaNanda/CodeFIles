from playwright.sync_api import sync_playwright
import time

from playwright.wait_mech import browser

# with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#
#         page.goto('https://the-internet.herokuapp.com/context_menu')
#         time.sleep(3)
#         box = page.locator("div#hot-spot")
#
#         box.click(button='right')
#         time.sleep(3)
#
#         browser.close()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context= browser.new_context()
    page= context.new_page("https://the-internet.herokuapp.com/key_presses?")
    page.click('input#target')

    page.keyboard.press('Enter')
    
    browser.close()

    page.goto()