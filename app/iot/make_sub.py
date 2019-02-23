import datetime
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from sqlalchemy.sql import exists

from . import db
from iot.models import Subscriber
from iot.forms import SubscribeForm
from iot.services import twilio_service
bp = Blueprint('subscribe', __name__)
@bp.route('/subscribe', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        form = SubscribeForm(request.form)
        form_submission = request.form.to_dict()
        phone_exists = db.session.query(exists().where(Subscriber.phone_number == form_submission['phone_number'])).scalar()
        if phone_exists is False and form.validate_on_submit():
            sub = Subscriber(phone_number=form_submission['phone_number'], device=form_submission['device'], contact_method=form_submission['contact_method'])
            db.session.add(sub)
            db.session.commit()
            flash('Subscription procssed for {}'.format(form.phone_number.data))
            return redirect('/')
        flash('Form is not valid, Phone number already exists {}'.format(phone_exists))
        return redirect('/')
    return redirect('/')