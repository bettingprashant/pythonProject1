# Password - Store the password in the Framework ?

from dotenv import load_dotenv
import os

def test_update_req():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(username)
    print(password)