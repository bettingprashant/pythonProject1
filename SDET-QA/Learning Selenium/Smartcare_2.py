# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj= Service("C:/DRIVER/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://www.smartcare.health/login")
# # driver.find_element(By.LINK_TEXT, "Login").click()
# driver.find_element(By.XPATH, "//input[@placeholder='Mobile/Email/User Id']").send_keys("surendra@konsultsoft.com")
# driver.find_element(By.XPATH, "//div[@class='col-lg-2 col-2']//*[name()='svg']").click()
# driver.find_element(By.XPATH, "(//input[@placeholder='Password'])[1]").send_keys("Test@123")
#
#
#
# time.sleep(10)
#
#

import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Setup Chrome WebDriver
driver = webdriver.Chrome


def test_smartcare():
    try:
    # Open the login page
        driver.get("https://www.smartcare.health/login")

    # Wait for the email input to be present and send keys
        email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Mobile/Email/User Id']"))
        )
        email_input.send_keys("surendra@konsultsoft.com")

    # Click the icon to switch to password input
        toggle_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='col-lg-2 col-2']//*[name()='svg']"))
        )
        toggle_icon.click()

    # Wait for the password input to be present and send keys
        password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='Password'])[1]"))
        )
        password_input.send_keys("Test@123")

    # Optionally, click the login button
        login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='bg-blue br-20px px-4 py-2 cursor-pointer wcolor']"))
        )
        login_button.click()

        user_role = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='role-manage-list-card doctor-color']//div[@class='role-select']"))
        )
        user_role.click()

        patient_list = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[5]//a[1]//div[1]//span[1]//img[1]"))
        )
        patient_list.click()

        new_patient = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Add New Patients')]"))
        )
        new_patient.click()






    # Wait for some time to observe the result
        time.sleep(10)

    except TimeoutException:
            print("An element was not found or took too long to appear.")
    finally:
    # Close the browser
            driver.quit()
