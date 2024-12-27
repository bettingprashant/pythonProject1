import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(20)
driver.maximize_window()

# windowid = driver.current_window_handle
# print(windowid)

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowIDs = driver.window_handles

# Approach 1
# parentwindowsid = windowIDs[0]
# childwindowsid = windowIDs[1]
# print(parentwindowsid,childwindowsid)
# # print(childwindowsid)
# driver.switch_to.window(childwindowsid)
# print(driver.title)
#
# driver.switch_to.window(parentwindowsid)
# print(driver.title)

# Approach 2
for winid in windowIDs:
    driver.switch_to.window(winid)
    print(driver.title)

time.sleep(5)