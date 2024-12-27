import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
# driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("05/30/2022")

year = "2020"
month = "March"
date = "30"
driver.find_element(By.XPATH,"//*[@id='datepicker']").click()

while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mon == month and yr == year:
        break;
    else:
        # driver.find_element(By.XPATH,"//a[@title='Next']").click()
        driver.find_element(By.XPATH,"//a[@title='Prev']").click()

dates = driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")
for ele in dates:
    if ele.text == date:
        ele.click()
        break


time.sleep(5)
driver.quit()