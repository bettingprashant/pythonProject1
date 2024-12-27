import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
country = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(country))

for countries in country:
    if countries.text == "Algeria":
        countries.click()
        break

time.sleep(5)