import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

noOfRows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
noOfColumns = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th")
print(len(noOfRows))
print(len(noOfColumns))

data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(data)

print("Printing all the rows and column data ................................")

# for r in range(2, 8):
#     for c in range(1, 5):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end="       ")



for r in range(2,8):
    authorname = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorname == "Mukesh":
        bookname = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print(bookname,"       ",authorname,"       ",price)


time.sleep(5)
driver.quit()
