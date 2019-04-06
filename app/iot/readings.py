import datetime
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session, abort
)
from sqlalchemy.sql import exists

from . import db
from iot.models import Device, DeviceReading
bp = Blueprint('readings', __name__)

@bp.route('/readings/<int:device_id>', methods=('GET', 'POST'))
def device_readings(device_id):
    device = db.session.query(Device).filter(Device.id == device_id).one_or_none()
    if device is not None:
        readings = db.session.query(DeviceReading).filter(DeviceReading.device == device.id).order_by(DeviceReading.id.desc())[:100]
        if readings is not None:
            all_readings = [reading.reading_mm for reading in readings]
            max_value = max(all_readings)
            max_reading = readings[all_readings.index(max_value)]
            return render_template('readings.html', device=device, readings=readings, max_reading=max_reading)
    return abort(404)

# TODO add download to csv/json route#