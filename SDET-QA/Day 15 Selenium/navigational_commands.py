import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.snapdeal.com")
driver.get("https://www.amazon.in")
driver.back()
driver.forward()
driver.refresh()

driver.quit()