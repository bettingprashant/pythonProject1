import allure
import pytest
import requests

@allure.title("TC#1 - Create Booking CRUD Positive")
@allure.description("TC#1- Verify the create Booking!")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url+base_path
    headers = {"Content-Type":"application/json"}
    payload = {
        "firstname": "Prashant",
        "lastname": "Raj",
        "totalprice": 123,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Free breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200
    responseData = response.json()

    bookingid = responseData["bookingid"]
    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

    firstname = responseData["booking"] ["firstname"]
    lastname = responseData["booking"]["lastname"]
    totalprice = responseData["booking"]["totalprice"]
    depositpaid = responseData["booking"]["depositpaid"]

    assert firstname == "Prashant"
    assert lastname == "Raj"
    assert totalprice == 123
    assert depositpaid == False


@allure.title("TC#2 Create Booking CRUD Negative")
@allure.description("TC#2 - Verify Booking is not created with {} data")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url+base_path
    headers = {"Content-Type":"application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    assert response.status_code == 500

@allure.title("TC#3 Negative Create Booking CRUD")
@allure.description("TC#2 - Verify Booking is not created with string value") #Bug Raise to Dev.
@pytest.mark.crud
def test_create_booking_negative_tc3():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Prashant",
        "lastname": "Raj",
        "totalprice": "Raj",
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Free breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)