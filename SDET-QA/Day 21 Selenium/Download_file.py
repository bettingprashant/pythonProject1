import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("https://www.tutorialspoint.com/selenium/practice/upload-download.php")
driver.maximize_window()

# driver.find_element(By.XPATH,"//a[@id='downloadButton']").click()
driver.find_element(By.XPATH,"//input[@id='uploadFile']").send_keys("C:/Users/91771/Downloads/Sample_01.jpeg")

time.sleep(5)
