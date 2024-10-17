# # from selenium import webdriver
# #
# # driver = webdriver.Chrome(executable_path=)
# #
# # driver.get("https://rcvacademy.com")
#
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# # Specify the path to the chromedriver executable
# service = Service("C:\\DRIVER\\chromedriver-win64\\chromedriver.exe")
#
# # Create an instance of the WebDriver
# driver = webdriver.Chrome(service=service)
# driver.get("https://rcvacademy.com")
# driver.maximize_window()
# print(driver.title)
# driver.close()



import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\DRIVER\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(service=service_obj)

# driver = webdriver.Chrome()

driver.get("https://smartcare.health")

time.sleep(20)