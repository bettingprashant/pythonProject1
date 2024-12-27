import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@value='Login']").click()
alert = driver.switch_to.alert
time.sleep(10)
alert.accept()

