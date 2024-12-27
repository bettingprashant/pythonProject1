import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.XPATH,"//*[@type='email']").clear()
driver.find_element(By.XPATH,"//*[@type='email']").send_keys("admin@yourstore.com")
driver.find_element(By.XPATH,"//*[@type='password']").clear()
driver.find_element(By.XPATH,"//*[@type='password']").send_keys("admin")
driver.find_element(By.XPATH,"//*[@type='submit']").click()
act_title = driver.title
ext_title = "OrangeHRM"

if act_title == ext_title:
    print("Test passed")
else:
    print("Test Fail")

time.sleep(20)
driver.quit()


