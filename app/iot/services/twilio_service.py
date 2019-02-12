from twilio.rest import Client
from iot.models import Subscriber
from flask import current_app as app
from iot import db

def send_sms(subscriber_id):
    subscriber = db.session.query(Subscriber).filter(Subscriber.id==subscriber_id).one()
    print(subscriber)
    client = generate_twilio_client()
    if subscriber is not None:
        message = client.messages.create(
            to="+1{}".format(subscriber.phone_number), 
            from_="+17866717356",
            body="Maybe take the long way home as it seems to be flooding")
        return message.sid
    else:
        raise Exception

def verify_caller_id(user_id):
    client = generate_twilio_client()
    validation_request = client.validation_requests \
                           .create(
                                friendly_name='My Home Phone Number',
                                phone_number='+1(305) 301-1347‬'
                            )

    print(validation_request)
    return validation_request.phone_number

def generate_twilio_client():
    account_sid = app.config['TWILIO_ACCOUNT_ID']
    auth_token = app.config['TWILIO_SECRET_KEY']
    return Client(account_sid, auth_token)
