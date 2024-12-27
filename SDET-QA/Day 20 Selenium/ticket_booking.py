import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
act = ActionChains(driver)
driver.find_element(By.XPATH,"//input[@id='product_549']").click()
driver.find_element(By.XPATH,"//input[@id='travname']").send_keys("Prashant")
driver.find_element(By.XPATH,"//input[@id='travlastname']").send_keys("Raj")
driver.find_element(By.XPATH,"//input[@id='dob']").click()

month = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
month.select_by_visible_text("Dec")

year = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
year.select_by_visible_text("1996")

dates = driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text == "25":
        ele.click()
        break

driver.find_element(By.XPATH,"//input[@id='sex_1']").click()
driver.find_element(By.XPATH,"//input[@id='fromcity']").send_keys("Delhi")
driver.find_element(By.XPATH,"//input[@id='tocity']").send_keys("Patna")

driver.find_element(By.XPATH,"//input[@id='departon']").click()
month = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
month.select_by_visible_text("Dec")

year = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
year.select_by_visible_text("2024")

dates = driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text == "25":
        ele.click()
        break

driver.find_element(By.XPATH,"//input[@id='billing_phone']").send_keys("9876543210")
driver.find_element(By.XPATH,"//input[@id='billing_email']").send_keys("abc@gmail.com")
driver.find_element(By.XPATH,"//input[@id='billing_address_1']").send_keys("Noida sec 62")
driver.find_element(By.XPATH,"//input[@id='billing_city']").send_keys("Noida")
driver.find_element(By.ID, "select2-billing_state-container").click()
state_option = driver.find_element(By.XPATH, "//li[contains(text(),'Uttar Pradesh')]")
state_option.click()
driver.find_element(By.XPATH,"//input[@id='billing_postcode']").send_keys("201301")


time.sleep(5)
driver.quit()