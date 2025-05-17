from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver= webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

''' Alert
name= driver.find_element(By.ID, 'name')
name.send_keys('soubhagya')

alert_button = driver.find_element(By.ID, 'alertbtn').click()
time.sleep(2)

alert = Alert(driver)
alert.accept()
'''

#popup
name= driver.find_element(By.ID, 'name')
name.send_keys('soubhagya')
time.sleep(2)
pop_btn= driver.find_element(By.ID, 'confirmbtn').click()
time.sleep(2)
alert = Alert(driver)
# alert.accept()

text_from_alert = alert.text
print(text_from_alert)
alert.dismiss()
time.sleep(3)


time.sleep(5)
driver.close()