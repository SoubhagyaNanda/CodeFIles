from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#webpage
driver= webdriver.Chrome()
driver.maximize_window()

#Link
urls = "https://www.odoo.com/web/login"
driver.get(urls)
time.sleep(5)

# Value
email= "soubhagyaranjannanda360@gmail.com"
password= "wejfij"

# Locator
email_loc= "(//input[@id='login'])[1]"
password_loc= "(//input[@id='password'])[1]"
login_loc= "button[type='submit']"

email_input= driver.find_element(By.XPATH, email_loc)
# assert email_input.is_displayed()
password_input= driver.find_element(By.XPATH, password_loc)
# assert password_input.is_displayed()

login_btn= driver.find_element(By.CSS_SELECTOR, login_loc)
# assert login_btn.is_displayed()

# Sending Values
email_input.send_keys(email)
password_input.send_keys(password)
login_btn.click()
time.sleep(5)

# URL check
expected_url = urls  # Adjust based on your Odoo instance
assert expected_url in driver.current_url, "Login failed or wrong redirection"

# Reset Password
reset_link= driver.find_element(By.LINK_TEXT, "Reset Password")
assert reset_link.is_displayed()
reset_link.click()
time.sleep(2)
assert "reset_password" in driver.current_url, "Reset Password link did not navigate correctly"
driver.back()
time.sleep(3)

# Don't have an account
signup_link= driver.find_element(By.LINK_TEXT, "Don't have an account?")
assert signup_link.is_displayed(), "Signup link is not visible"
signup_link.click()
time.sleep(2)

assert "signup" in driver.current_url, "Signup link did not navigate correctly"
driver.back()
time.sleep(2)

# fa fa-eye
password_input= driver.find_element(By.XPATH, password_loc)
password_input.send_keys('password123')
time.sleep(1)

eye_icon = driver.find_element(By.XPATH, "(//i[@class='fa fa-eye'])[1]")
assert eye_icon.is_displayed(), "Eye icon is not visible"
eye_icon.click()
time.sleep(1)


# logo displayed
logo = driver.find_element(By.XPATH, "(//img[@alt='Logo'])[1]")
assert logo.is_displayed(), "Logo is not displayed"


# footer
footer_link= driver.find_element(By.LINK_TEXT, "Powered by")
assert footer_link.is_displayed(), "Footer link is not visible"

driver.close()