# This is not working I am using this for myself



import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
act = ActionChains(driver)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

drag_ele = driver.find_element(By.XPATH,"//div[@id='draggable']")
drop_ele = driver.find_element(By.XPATH,"//div[@id='droppable']")

act.drag_and_drop(drag_ele,drop_ele).perform()