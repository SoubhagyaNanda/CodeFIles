import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


print(dir(selenium))
driver = webdriver.Chrome()
driver.get('https://www.facebook.com/login/')

email= driver.find_element(By.ID, "email")
email.send_keys('soubhagya@gmail.com')
time.sleep(5)
driver.quit()