import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

driver.find_element(By.XPATH,"//li[1]//a[1]//span[1]").click()
driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Users']").click()

rows = driver.find_elements(By.XPATH,"//div[@class='orangehrm-container']")

time.sleep(3)