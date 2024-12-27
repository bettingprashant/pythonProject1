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

point_me = driver.find_element(By.XPATH,"//*[@id='HTML3']/div[1]/div/button")
act.move_to_element(point_me).click().perform()
time.sleep(5)