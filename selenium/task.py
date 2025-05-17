import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import json


driver= webdriver.Chrome()

file_path= os.path.abspath('task_eco.html')

driver.get(file_path)

'''# ROW COUNT
with open('task_data.json', 'r') as fo:
    data= fo.read()
    expectedResult= json.loads(data)

actual_row_count = driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
assert expectedResult['row_count'] == len(actual_row_count)'''

# check how many product buy an indivisual customer and price, propduct_name:- provide customer name

# indivisual_cum= driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
name= 'User966'
product= driver.find_elements(By.XPATH, f"//tr/td[text()='{name}']/following-sibling::td[2]")
print(len(product))
driver.close()
# price = driver.find_elements(By.XPATH, '//tr/td[5]')

# time.sleep(2)
# driver.quit()