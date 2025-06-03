import time

from playwright.sync_api import sync_playwright

'''with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("'https://the-internet.herokuapp.com/windows/new")
    time.sleep(3)

    with context.expect_page() as newInfo:
        time.sleep(3)
        page.click("a[href='/windows/new']")

    newPage= newInfo.value # It will give the new page values
    print(newPage)
    time.sleep(3)

    print('first page:',page.title())
    print('second page:', newPage.title())


    print(newPage.locator("//h3[text()='New Content']")).text_content()
    
    newPage.close()

    browser.close()'''


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page1 = context.new_page()
    page1.goto("'https://the-internet.herokuapp.com/windows")


    with context.expect_page() as new:
        page1.click("//h3[text()='New Content']")

    page2= new.value
    allPage= context.pages

    for index, value in enumerate(allPage):
        print(f'page number {index+1}: {value}')


    # Switch to page1
    page1.bring_to_front()
    print(page1.url)

    # Switch to page2
    page2.bring_to_front()
    print(page2.url)

    browser.close()