import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("https://the-internet.herokuapp.com/upload")
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys("C:/Movies/Sample_01.jpeg")
driver.find_element(By.XPATH,"//input[@id='file-submit']").click()

# driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
# driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
#
# driver.find_element(By.XPATH,"//span[normalize-space()='PIM']").click()
# driver.find_element(By.XPATH,"//a[normalize-space()='Add Employee']").click()
# driver.find_element(By.XPATH,"//button[@class='oxd-icon-button oxd-icon-button--solid-main employee-image-action']").send_keys("C:/Users/91771/Downloads/Sample_01.jpeg")
time.sleep(5)
