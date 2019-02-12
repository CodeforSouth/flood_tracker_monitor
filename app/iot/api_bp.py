import datetime
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort
import json


from . import db
from iot.models import Device
from iot.forms import SubscribeForm

bp = Blueprint('api', __name__)
@bp.route('/api/devices', methods=('GET', 'POST'))
def create():
        devices  = db.session.query(Device).all()
        return jsonify(data=[device.serialize for device in devices])

