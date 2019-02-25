from datetime import datetime
from authy.api import AuthyApiClient
from iot.models import Subscriber
from flask import current_app as app
from iot import db

def allowed_to_send(subscriber):
    time_delta = datetime.utcnow() - subscriber.last_contacted
    value = (subscriber.verified) and (not subscriber.opted_out) and (time_delta.seconds >= (60 * 60))
    return value

def send_sms(subscriber_id):
    subscriber = db.session.query(Subscriber).filter(Subscriber.id==subscriber_id).one()
    client = generate_twilio_client()
    if subscriber and allowed_to_send(subscriber):
        message = client.messages.create(
            to="+1{}".format(subscriber.phone_number), 
            from_="+17866717356",
            body="Maybe take the long way home as it seems to be flooding")
        return message.sid
    return False

def verify_phone_start(phone_number, method):
    if phone_number is not None:
        authy_api = AuthyApiClient(app.config['TWILIO_VERIFY_SECRET_KEY'])
        verification = authy_api.phones.verification_start(
                phone_number,
                '1',
                method
            )
    return True

def verify_phone_check(phone_number, token):
    if phone_number is not None:
        authy_api = AuthyApiClient(app.config['TWILIO_VERIFY_SECRET_KEY'])
        verification = authy_api.phones.verification_check(
                phone_number,
                '1',
                token
            )
        return verification

def generate_twilio_client():
    account_sid = app.config['TWILIO_ACCOUNT_ID']
    auth_token = app.config['TWILIO_SECRET_KEY']
    return Client(account_sid, auth_token)
