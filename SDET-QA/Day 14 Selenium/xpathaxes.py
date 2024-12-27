import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()
text_msg = driver.find_element(By.ID,"//tbody/tr[25]/td[1]").text
print(text_msg)