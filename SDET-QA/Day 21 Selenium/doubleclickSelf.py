# This is working I am using this for myself practice



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

field1 = driver.find_element(By.XPATH,"//input[@id='field1']")
field1.clear()
field1.send_keys("Welcome")

copy = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
# field2 = driver.find_element(By.XPATH,"")
act.double_click(copy).click().perform()
time.sleep(5)