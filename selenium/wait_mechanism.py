from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/cart")
driver.implicitly_wait(5)

search = driver.find_element(By.XPATH, "//input[@type='search']")
search.send_keys('er')

time.sleep(2)
addtocart = driver.find_elements(By.XPATH, "//div[@class='products']/div//button")

for click in addtocart:
    click.click()

cart_img = driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
# time.sleep(2)
proceedtocheck= driver.find_element(By.XPATH, "//button[text()= 'PROCEED TO CHECKOUT']").click()
# time.sleep(2)

promoCode = driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys('jbhjbdc')

apply = driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()

'''invalid_code= driver.find_element(By.XPATH, "//span[@class='promoInfo']")
print(invalid_code.text)'''

wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))

time.sleep(3)
driver.close()

