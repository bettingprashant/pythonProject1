import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")

driver.switch_to.frame("iframeResult")
field1 = driver.find_element(By.XPATH,"//input[@id='field1']")
field1.clear()
field1.send_keys("welcome")

copy = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

act = ActionChains(driver)
act.double_click(copy).perform()

time.sleep(5)
driver.quit()