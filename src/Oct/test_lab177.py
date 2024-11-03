#Create Booking TC
# VErify that booking is not null
# status code

import pytest
import allure
import requests

@allure.title("Test GET Request - Restful BOOKER Project#1")
@allure.description("TC#1 -> Verify that GET Request with ID works")
@allure.tag("regression","p0", "smoke")
@allure.label("owner","Prashant Raj")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.text)
    print(response_data.json())
    print(response_data.headers)
    assert response_data.status_code==200

@allure.title("Test GET Request - Restful BOOKER Project#2")
@allure.description("TC#2 -> Verify that GET Request with invalid booking id works or not")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url)
    assert response_data.status_code == 404

@allure.title("Test GET Request - Restful BOOKER Project#3")
@allure.description("TC#2 -> Verify that GET Request with invalid char booking works or not")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response_data = requests.get(url)
    assert response_data.status_code == 404