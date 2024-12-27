import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import  os

driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(5)
# driver.save_screenshot(r"C:/Users/91771\OneDrive - SmartCare Analytica AB/Desktop/Python Automtion/Python Selenium/pythonProject1/SDET-QA/Day 23 Selenium/home.png")
driver.save_screenshot(os.getcwd() +"\\home.png")
# driver.get_screenshot_as_file(os.getcwd() +"\\home.png")