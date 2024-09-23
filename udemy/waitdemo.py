# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj = Service("C:/DRIVER/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
# results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
# count = len(results)
# assert count > 3
# for result in results:
#     result.find_element(By.XPATH,"div/button").click()
#
# driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
# driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# driver.find_element(By.CSS_SELECTOR, "promocode").send_keys("rahulshettyacademy")
# driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
# print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
#
# time.sleep(10)
import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(5)


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum= 0
for price in prices:
    sum = sum + int(price.text)
print(sum)
totalAmount = driver.find_element(By.CSS_SELECTOR,".totAmt").text

assert sum == totalAmount

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)


