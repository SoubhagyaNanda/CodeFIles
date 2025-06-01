from click import pass_context
from playwright.sync_api import sync_playwright
import time
def run(playwright):
    browser= playwright.webkit.launch(headless=False)
    context= browser.new_context()
    page= context.new_page()

    page.goto('https://the-internet.herokuapp.com/')
    # print(page.title())
    #
    # page.set_viewport_size({"width": 12800, "hight":72000})
    #
    # time.sleep(3)

    #Scroll down
    # page.evaluate("window.scrollTo(0,document.body.scrollHeight);")
    # time.sleep(2)

    #Dropdown

    '''page.goto('https://the-internet.herokuapp.com/')
    dropdown= page.locator("#dropdown")
    time.sleep(3)
    dropdown.select_option("2") # selected option with value2

    selected= dropdown.input_value()
    print(f'selected dropdown value {selected}')
    time.sleep(3)'''

    # Verification
   ''' 
   if selected==2:
        return 'pass'
   return 'Failed'
   '''

    # Assertion
    # assert selected==3 , 'data not matched'

    # alert
'''    page.goto('https://the-internet.herokuapp.com/javascript_alerts')
    def handel_dialog(dialog):
        print(f'dialog message{dialog.message}')
        dialog.accept()
    page.on(handle_dialog)
    page.click("text=Click for JS Alert")'''

    # File upload
    page.goto('https://the-internet.herokuapp.com/upload')
    file_input= page.locator("#input#file-upload")
    file_path= r'uploadFilePath'

    file_input.set_input_files(file_path) # Used to send files.

    page.click("input#file-submit")

    time.sleep(3)
    print(page.locator('div#uploaded-files').text_content().strip())
with sync_playwright() as playwright:
    run(playwright)