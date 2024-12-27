import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains (@id,'day')]")

# Approach 1
# for checkbox in checkboxes:
#     if not checkbox.is_selected():
#         checkbox.click()
# assert  checkbox.is_selected()

# Approach 2

# for i in range (len(checkboxes)):
#     checkboxes[i].click()

# Approach 3
#
# for checkbox in checkboxes:
#     checkbox.click()

# 4 Select Multiple checkbox with choice

for checkbox in checkboxes:
    weekdays = checkbox.get_attribute("id")
    if weekdays == 'monday' or weekdays == 'sunday' or weekdays == 'thursday':
        checkbox.click()

# 5 select last 2 checkboxes

# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()


time.sleep(10)
driver.quit()