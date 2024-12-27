import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
mywait = WebDriverWait(driver,10)
# mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=Exception) #Polling is used for fast execution, Exception is used for handle the Exception
driver.get("https://www.google.com/")

searchbox = driver.find_element(By.NAME,"q")
searchbox.send_keys("Selenium")
searchbox.submit()

searchlink = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()
driver.quit()