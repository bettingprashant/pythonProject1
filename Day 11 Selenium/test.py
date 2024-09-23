# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
#
# time.sleep(100)
# driver.close()



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj=Service(executable_path=r"C:/DRIVER/chromedriver-win64/chromedriver")
driver= webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com")
