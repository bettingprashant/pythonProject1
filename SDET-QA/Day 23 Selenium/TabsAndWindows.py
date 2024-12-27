import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(15)
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
#
#
# driver.find_element(By.LINK_TEXT,"Register").send_keys(Keys.CONTROL+Keys.RETURN)

# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://www.orangehrm.com/")

driver.get("https://www.opencart.com/")
driver.switch_to.new_window('window')
driver.get("https://www.orangehrm.com/")

time.sleep(5)
