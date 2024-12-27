import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")

# element = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys("Apple Macbook pro 13-inch")
# element = driver.find_element(By.XPATH,"//div[@class='footer']//a")
# element.text
#
# login_element = driver.find_element(By.LINK_TEXT,"Log in")
# login_element.click()

# elements = driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# elements[0].send_keys("Apple Macbook pro 13-inch")

# elements = driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(elements))
# # print(elements[0].text)
# for ele in elements:
#     print(ele.text)

elements = driver.find_elements(By.LINK_TEXT,"Log")
print("elements returned", len(elements))