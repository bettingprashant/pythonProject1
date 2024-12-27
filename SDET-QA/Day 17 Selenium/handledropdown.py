import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.opencart.com/")
driver.implicitly_wait(20)

# drpcountry_ele = driver.find_element(By.XPATH,"//select[@id='input-country']")
driver.maximize_window()
register = driver.find_element(By.XPATH,"//a[@class='btn btn-black navbar-btn']")
register.click()
time.sleep(30)
drpcountry = Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))
drpcountry.select_by_visible_text("India")
# drpcountry.select_by_value("7")
# drpcountry.select_by_index(13)