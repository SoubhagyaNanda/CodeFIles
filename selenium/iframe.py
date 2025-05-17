from  selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.switch_to.frame('courses-iframe')

time.sleep(3)

click_courses= driver.find_element(By.LINK_TEXT, 'Courses')
click_courses.click()
time.sleep(3)

driver.switch_to.default_content()


driver.close()