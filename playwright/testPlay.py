from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    print(dir(p))
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # navigate to the browser
    page.goto('https://www.youtube.com/4')
    page.pause()
    browser.close()

'''def login(email,password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://www.facebook.com/login/')
        page.fill("//input[@id='email']", email)
        page.fill("//input[@id='pass]",password)

        page.click("//button[@id='loginbutton']")

        page.screenshot(path='fblogin.png')
        page.wait_for_timeout(5000)
        browser.close()

login('email@gmail.com', 'sdchjbdcvsd')'''