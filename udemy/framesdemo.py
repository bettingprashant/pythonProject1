
# from selenium import webdriver
#
# driver= webdriver.Chrome()
# driver.get("http://the-internet.herokuapp.com/windows")
# driver.maximize_window()
# driver.implicitly_wait(2)

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("http://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")






