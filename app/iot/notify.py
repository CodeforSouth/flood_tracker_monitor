import datetime
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort, jsonify
)
from sqlalchemy.sql import exists
import phonenumbers
import json
from iot import db
from iot.models import Subscriber, Device
from iot.forms import SubscribeForm
from iot.services.validate_partice_webhook import request_is_from_particle
from iot.services.twilio_service import send_sms


bp = Blueprint('notify', __name__)
@bp.route('/notify',methods=('GET', 'POST'))
def notify():
        if request.method == 'POST':
            #TODO replace valid_request hardcode
            valid_request =  False
            # valid_request = request_is_from_particle(request)
            if valid_request:
                hook_data = request.get_json()
                device = db.session.query(Device).filter(Device.core_id == hook_data['core_id']).one_or_none()
                if device is not None:
                    subcribers_for_device = db.session.query(Subscriber).filter(Subscriber.device == device.id).all()
                    for subscriber in subcribers_for_device:
                        send_sms(subscriber.id)
                    return jsonify(success=True)
                return abort(400)
            return abort(401)
        return redirect('/')
