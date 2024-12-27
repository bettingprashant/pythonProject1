import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
act = ActionChains(driver)

min_value = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
max_value = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")


print("Before execution ------------")
print(min_value.location)
print(max_value.location)

act.drag_and_drop_by_offset(min_value,59,0).perform()
act.drag_and_drop_by_offset(max_value,-39,0).perform()

print("Aftter Execution value -----------")
print(min_value.location)
print(max_value.location)




