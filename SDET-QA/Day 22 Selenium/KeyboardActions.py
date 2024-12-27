import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://text-compare.com/")
driver.maximize_window()
act = ActionChains(driver)
driver.implicitly_wait(10)

input1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
input1.send_keys("Welcome to Selenium")

# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

act.send_keys(Keys.TAB)
act.perform()

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(5)






