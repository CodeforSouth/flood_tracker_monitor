import datetime
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from . import db
from iot.models import Subscriber
from iot.forms import SubscribeForm
from iot.services import twilio_service
bp = Blueprint('subscribe', __name__)
@bp.route('/subscribe', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        form = SubscribeForm()
        if form.validate_on_submit():
            flash('Subscription being procssed for {}'.format(form.phone_number.data))
            return redirect('/')
        return render_template('blog/create.html')
    return render_template('blog/create.html')