# payments/mpesa.py
import requests
import base64
from datetime import datetime

def initiate_stk_push(phone, amount, order_id, access_token=None):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "BusinessShortCode": "174379",
        "Password": "your_encoded_password",
        "Timestamp": "20230814123456",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": "174379",
        "PhoneNumber": phone,
        "CallBackURL": "https://yourdomain.com/callback",
        "AccountReference": f"Order{order_id}",
        "TransactionDesc": "Property Payment"
    }

    response = requests.post(
        "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest",
        headers=headers,
        json=payload
    )
    return response.json()


# payments/mpesa.py
import os
import requests
from django.conf import settings


def generate_password(business_shortcode, passkey):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    data = f"{business_shortcode}{passkey}{timestamp}"
    return base64.b64encode(data.encode()).decode()

def get_current_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S")


def initiate_stk_push(phone, amount, order_id):
    config = settings.MPESA_CONFIG

    headers = {
        "Authorization": f"Bearer {generate_access_token()}",
        "Content-Type": "application/json"
    }

    payload = {
        "BusinessShortCode": config['BUSINESS_SHORTCODE'],
        "Password": generate_password(config['BUSINESS_SHORTCODE'], config['PASSKEY']),
        "Timestamp": get_current_timestamp(),
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": config['BUSINESS_SHORTCODE'],
        "PhoneNumber": phone,
        "CallBackURL": config['CALLBACK_URL'],
        "AccountReference": f"Order{order_id}",
        "TransactionDesc": "Property Payment"
    }

    response = requests.post(
        "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest",
        headers=headers,
        json=payload
    )
    return response.json()


def generate_access_token():
    config = settings.MPESA_CONFIG
    auth = (config['CONSUMER_KEY'], config['CONSUMER_SECRET'])
    response = requests.get(
        "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials",
        auth=auth
    )
    return response.json()['access_token']