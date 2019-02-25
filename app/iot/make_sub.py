import datetime
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort
from sqlalchemy.sql import exists
import phonenumbers

from . import db
from iot.models import Subscriber
from iot.forms import SubscribeForm, VerifySubscribeForm
from iot.services import twilio_service
from iot.tasks import send_async_phone_verification
bp = Blueprint('subscribe', __name__)
@bp.route('/subscribe', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        form = SubscribeForm(request.form)
        session.get("phone_number")
        try:
            user_phone_number = phonenumbers.parse(form.phone_number.data, 'US')
        except phonenumbers.phonenumberutil.NumberParseException:
            flash('{} is not a valid US number'.format(form.phone_number.data[:10]))
        if phonenumbers.is_valid_number(user_phone_number):
            phone_exists = db.session.query(exists().where(Subscriber.phone_number == user_phone_number.national_number)).scalar()
            if phone_exists is False and form.validate_on_submit():
                sub = Subscriber(phone_number=user_phone_number.national_number, device=form.device.data, contact_method=form.contact_method.data)
                #TODO user selected notification method
                session['phone_number'] = user_phone_number.national_number
                db.session.add(sub)
                db.session.commit()
                send_async_phone_verification(sub.phone_number, 'sms')
                flash('Subscription processing for {}'.format(form.phone_number.data))
                return render_template('verify_number.html', phone_number=sub.phone_number, form=VerifySubscribeForm())
            flash('Phone number already exists, please email floodtracking@codeformiami.org')
            return redirect('/')
        flash('{} is not a valid US number'.format(form.phone_number.data[:10]))
        return redirect('/')
    return redirect('/')

@bp.route('/verify', methods=('GET', 'POST'))
def verify():
    if request.method == 'POST':
        form = VerifySubscribeForm(request.form)
        phone_number = session.get("phone_number")
        if phone_number:
            phone_exists = db.session.query(exists().where(Subscriber.phone_number == phone_number)).scalar()
            if phone_exists is True and form.validate_on_submit():
                sub = db.session.query(Subscriber).filter(Subscriber.phone_number == phone_number).one_or_none()
                verification = twilio_service.verify_phone_check(phone_number, form.verification_code.data)
                if verification.ok():
                    sub.verified = True
                    db.session.add(sub)
                    db.session.commit()
                    flash('Phone Number Verified'.format(phone_number))
                    return redirect('/')
                else:
                    for error_msg in verification.errors().values():
                        flash('Error Message: '.format(error_msg))
                    return redirect('/')
            flash('Phone number does not exist, please email floodtracker@codeformiami.org')
            return redirect('/')
        flash('Phone number not set, please email floodtracker@codeformiami.org')
        return redirect('/')
    return render_template('verify_number.html', phone_number=session.get("phone_number"), form=VerifySubscribeForm())