import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("Welcome")
# alert.accept()
alert.dismiss()
time.sleep(10)