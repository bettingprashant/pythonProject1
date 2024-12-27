import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
alllinks = driver.find_elements(By.TAG_NAME, 'a')
print(len(alllinks))
count = 0

for link in alllinks:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)

    except:
        None

        if res.status_code >= 400:
            print(url, "is broken link")
            count += 1
        else:
            print(url, "is Valid url")
print("Total number of broken links:", count)
