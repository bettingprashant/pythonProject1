

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name = "Raj"
service_obj = Service("C:/DRIVER/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains (driver)
# action.double_click(driver.find_element(By.))
# action.click_and_hold()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
