import requests
from requests.auth import HTTPBasicAuth
import json

# Your details from screenshot
LOCAL_URL = "http://10.209.130.137:8080/message"
USERNAME = "sms"
PASSWORD = "dn0IPgwS"

def send_sms(phone_number, message):
    payload = {
        "message": message,
        "phoneNumbers": [phone_number]
    }
    response = requests.post(
        LOCAL_URL,
        json=payload,
        auth=HTTPBasicAuth(USERNAME, PASSWORD)
    )
    print(response.status_code)
    print(response.text)

# Test - replace with real number
send_sms("+919876543210", "Hello from my SMSGate!")
