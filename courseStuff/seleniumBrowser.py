import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')

email_value= driver.find_element(By.ID, 'email')
email_value.send_keys('shjuhsuhv@gmail.com')
time.sleep(3)

driver.quit()