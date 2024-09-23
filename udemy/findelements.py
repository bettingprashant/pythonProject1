# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj = Service("C:/DRIVER/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://rahulshettyacademy.com/client")

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/DRIVER/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.makemytrip.com/")
driver.find_element(By.XPATH, "//")
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
time.sleep(2)
cities =driver.find_elements_by_css_selector("p[class*='blackText']")
print (len(cities))
for city in cities:
    if city.text =="Del Rio, United States":
        city.click()
        break


driver.find_element_by_xpath("//p[text()='Delhi, India']").click()