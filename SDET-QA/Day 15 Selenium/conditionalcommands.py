import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")
searchbox = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display status:",searchbox.is_displayed())
print("Display status:",searchbox.is_enabled())

rd_male = driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH,"//input[@id='gender-female']")

print(rd_male.is_selected())
print(rd_female.is_selected())

rd_male.click()
print("After slecting male rd Button")
print(rd_male.is_selected())
print(rd_female.is_selected())

rd_female.click()
print("after selecting Female rd button")
print(rd_female.is_selected())
print(rd_male.is_selected())

driver.close()