from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("'https://the-internet.herokuapp.com/iframe")

    frame= page.frame(name='mce_0_ifr')

    #Access and intracting with element inside the frame
    text_area = frame.locator('#tinymce')

    print(text_area.inner_text())

    page.screenshot(path='iframe_screenshot.png')
    browser.close()