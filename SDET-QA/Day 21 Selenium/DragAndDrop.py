import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

act = ActionChains(driver)

rome_ele = driver.find_element(By.ID,"box6")
italy_ele = driver.find_element(By.ID,"box106")
act.drag_and_drop(rome_ele,italy_ele).perform()

washington_ele = driver.find_element(By.ID,"box3")
usa_ele = driver.find_element(By.ID,"box103")
act.drag_and_drop(washington_ele,usa_ele).perform()