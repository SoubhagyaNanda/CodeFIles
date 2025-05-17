from  selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.expected_conditions import title_is

driver= webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.find_element(By.ID, 'openwindow').click()
main_window = driver.current_window_handle
all_window = driver.window_handles

for i in all_window:
    if i!=main_window:
        driver.switch_to.window(i)
        break
print(driver.title)
time.sleep(2)
driver.close()

driver.switch_to.window(main_window)
print(driver.title)
time.sleep(2)

time.sleep(3)
driver.quit()