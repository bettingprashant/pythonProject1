#Checkbox

# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
# for checkbox in checkboxes:
#     weekdays = checkbox.get_attribute("id")
#     if weekdays == 'tuesday' or weekdays == 'monday' or weekdays == 'sunday':
#         #     if weekdays == 'monday' or weekdays == 'sunday' or weekdays == 'thursday':
#         checkbox.click()
# time.sleep(10)

#Dropdown

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
country = Select (driver.find_element(By.XPATH,"//select[@id='country']"))
# country.select_by_value("canada")
# country.select_by_index(4)
country.select_by_visible_text("India")
time.sleep(10)
driver.quit()