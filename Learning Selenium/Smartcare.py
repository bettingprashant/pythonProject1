import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

time.sleep(20)






















# import time
#
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# service_obj= Service("C:/DRIVER/chromedriver-win64/chromedriver.exe")
# driver= webdriver.Chrome(service=service_obj)
#
# driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.find_element(By.NAME, "name").send_keys("Raj")
# driver.find_element(By.NAME,"email").send_keys("abc@gmail.com")
# driver.find_element(By.ID,"exampleInputPassword1").send_keys("Raj@1234")
# driver.find_element(By.ID, "exampleCheck1").click()
# dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# dropdown.select_by_index(1)
# driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
# driver.find_element(By.NAME, "bday").send_keys("19-08-1998")
# driver.find_element(By.XPATH, "//input[@value='Submit']").click()
# message=driver.find_element(By.CLASS_NAME, "alert-success").text
# print(message)
# time.sleep(10)

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:/DRIVER/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://rahulshettyacademy.com/client")
driver.get("https://www.smartcare.health")
driver.find_element(By.LINK_TEXT, "Login").click()
driver.find_element(By.XPATH, "//input[@placeholder='Mobile/Email/User Id']").send_keys("surendra@konsultsoft.com")






# driver.find_element(By.CSS_SELECTOR, "input[placeholder='Mobile/Email/User Id']").send_keys("pat@yopmail.com")

# driver.find_element(By.LINK_TEXT, "Forgot password?" ).click()
# driver.find_element(By.XPATH, "//input[@placeholder='Enter your email address']").send_keys("abc@gmail.com")
# driver.find_element(By.XPATH, "//input[@id='userPassword']").send_keys("Test@123")
# driver.find_element(By.XPATH, "//input[@id='confirmPassword']").send_keys("Test@123")
# driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(10)



