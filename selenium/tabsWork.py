from  selenium import webdriver
import time

driver= webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

time.sleep(3)

'''
# Tab switch

driver.execute_script("window.open('')")

tab = driver.window_handles
driver.switch_to.window(tab[1])
driver.get('https://www.youtube.com/')
time.sleep(2)

# Back to main window.
driver.switch_to.window(tab[0])
print('Back to main window')
'''

# without javascript execute
'''
open_tabs = driver.find_element(By.ID,'opentab').click()

tab= driver.window_handles
driver.switch_to.window(tab[1])

cour = driver.find_element(By.XPATH, '//a[text()="Courses"]').click()
time.sleep(2)
driver.switch_to.window(tab[0])
print('Back menu')
time.sleep(3)
'''


time.sleep(3)
# driver.close()
driver.quit()