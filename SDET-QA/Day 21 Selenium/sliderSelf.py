# This is not working I am using this for myself



import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
act = ActionChains(driver)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

min_value = driver.find_element(By.XPATH,"//div[@id='HTML7']//span[1]")
max_value = driver.find_element(By.XPATH,"//div[@id='HTML7']//span[2]")

print("Before Execution ..........................")

print(min_value.location)
print(max_value.location)

act.drag_and_drop_by_offset(min_value,30,0).click().perform()
act.drag_and_drop_by_offset(max_value,-30,0).click().perform()
print("After Execution ..........................")

print(min_value.location)
print(max_value.location)
time.sleep(8)