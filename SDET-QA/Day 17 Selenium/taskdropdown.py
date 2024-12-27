import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
dropdown_country = Select(driver.find_element(By.XPATH,"//select[@id='country']"))
dropdown_country.select_by_value("canada")
time.sleep(10)