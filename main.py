import os

from twilio.rest import Client
from dotenv import load_dotenv


def send_sms(text):

    load_dotenv()

    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body = text,  
        from_ = '+12055129864',  
        to = '+79819622766',  
        )

if __name__ == "__main__":
    send_sms("Hello, Fibletype")