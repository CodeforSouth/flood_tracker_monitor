import iso8601
from flask import (
    Blueprint, flash, g, redirect, request, jsonify, abort
)
import json
from sqlalchemy import exc

from iot import db
from iot.models import Device, DeviceReading
from iot.services.validate_partice_webhook import request_is_from_particle

#TODO consider moving this to mostly flask-restful

bp = Blueprint('api', __name__)
@bp.route('/api/devices', methods=('GET', 'POST'))
def create():
        devices  = db.session.query(Device).all()
        return jsonify(data=[device.serialize for device in devices])

@bp.route('/api/devices/<int:device_id>', methods=('GET', 'POST'))
def device_view(device_id):
    print(device_id)
    device = db.session.query(Device).filter(Device.id == device_id).one_or_none()
    readings = db.session.query(DeviceReading).filter(DeviceReading.device == device.id).order_by(DeviceReading.id.desc())[:10000]
    if readings is not None:
        return jsonify(data=[reading.serialize for reading in readings])
    else:
        return ([])


@bp.route('/api/reading_request', methods=('GET', 'POST'))
def reading_request():
    if request.method == 'POST':
        #TODO replace valid_request hardcode
        valid_request =  False
        valid_request = request_is_from_particle(request)
        if valid_request:
            hook_data = request.get_json()
            print(hook_data['coreid'])
            device = db.session.query(Device).filter(Device.core_id == int(hook_data['coreid'])).one_or_none()
            ## TODO consider auto-adding devices on valid_request
            print(device)
            print(hook_data['event'])
            if device is not None and hook_data['event'] == 'level_mm':
                try:
                    reading_cm = int(hook_data['data'])
                    reading_reported=iso8601.parse_date(hook_data['published_at'])
                except KeyError:
                    return abort(400)
                device_reading = DeviceReading(device=device, core_id=device.core_id, reading_cm=reading_cm, reading_reported=reading_reported)
                db.session.add(device_reading)
                db.session.commit()
                return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
            return abort(400)
        return abort(401)
    return redirect('/')

