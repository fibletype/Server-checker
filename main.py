import os
import logging
import requests

from time import sleep
from twilio.rest import Client
from dotenv import load_dotenv
from requests.exceptions import HTTPError

logging.basicConfig(level=logging.INFO)

def send_sms(text):

    load_dotenv()

    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(
            body = text,  
            from_ = os.getenv('FROM_NUMBER'),  
            to = os.getenv('TO_NUMBER'),  
            )
        logging.info('Message sent')
    except Exception:
        logging.error('Message is not sent')

def check_server(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError:
        send_sms('Site unavalibale')


if __name__ == "__main__":
    status = True
    while True:
        check_server('https://python101.online')
        sleep(120)
