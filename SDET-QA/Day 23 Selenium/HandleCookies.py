import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

cookies = driver.get_cookies()
print("size of Cookies :",len(cookies))
#
# for c in cookies:
#     # print(c)
#     print(c.get('name'),":",c.get('value'))

driver.add_cookie({"name":"MyCookie","value":"123456"})
cookies = driver.get_cookies()
print("size of Cookies after adding new:",len(cookies))

driver.delete_cookie("MyCookie")
cookies = driver.get_cookies()
print("size of Cookies after 1 delete:",len(cookies))

driver.delete_all_cookies()
cookies = driver.get_cookies()
print("size of Cookies after all delete:",len(cookies))

time.sleep(5)