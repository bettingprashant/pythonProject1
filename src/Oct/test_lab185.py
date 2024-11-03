import allure
import pytest
import requests

def test_update_req_1(create_token, create_booking_id):
    print("Token ->", create_token)
    print("Booking ID ->", create_booking_id)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking" +str(create_booking_id)

    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}