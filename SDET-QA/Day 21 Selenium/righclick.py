import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
button = driver.find_element(By.XPATH,"//*[@class='context-menu-one btn btn-neutral']")
act = ActionChains(driver)

act.context_click(button).perform()
driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click()
time.sleep(5)
driver.switch_to.alert.accept()