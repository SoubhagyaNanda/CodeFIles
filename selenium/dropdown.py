from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

select_locater= Select(driver.find_element(By.ID, 'dropdown-class-example'))

# select_locater.select_by_index(1)
# select_locater.select_by_value('option2')
select_locater.select_by_visible_text('Option1')
# select_locater.all_selected_options()

time.sleep(3)
select_locater.deselect_by_index(3)
time.sleep(3)
driver.quit()