import iso8601
from flask import (
    Blueprint, flash, g, redirect, request, jsonify, abort
)
from sqlalchemy import exc
from iot import db
from iot.models import Device, DeviceReading
from iot.services.validate_partice_webhook import request_is_from_particle
#TODO consider moving this to mostly flask-restful
#TODO use more of the flask-sqlalchemy helpers

bp = Blueprint('api', __name__)
@bp.route('/api/devices', methods=('GET', 'POST'))
def create():
        devices  = db.session.query(Device).all()
        return jsonify(data=[device.serialize for device in devices])

@bp.route('/api/devices/<int:device_id>', methods=('GET', 'POST'))
def device_view(device_id):
    device = db.session.query(Device).filter(Device.id == device_id).one_or_none()
    if device is not None:
        readings = db.session.query(DeviceReading).filter(DeviceReading.device == device.id).order_by(DeviceReading.id.desc())[:10000]
        if readings is not None:
            return jsonify(data=[reading.serialize for reading in readings])
    return jsonify(data=[])


@bp.route('/api/reading_request', methods=('GET', 'POST'))
def reading_request():
    # TODO
    if request.method == 'POST':
        if request_is_from_particle(request):
            hook_data = request.form.to_dict()
            if hook_data['coreid'] is not None:
                device = db.session.query(Device).filter(Device.core_id == hook_data['coreid']).one_or_none()
            else:
                device = None
            ## TODO consider auto-adding devices on valid_request
            if device is not None and hook_data['event'] == 'level_mm':
                try:
                    reading_mm = int(hook_data['data'])
                    reading_reported=iso8601.parse_date(hook_data['published_at'])
                except KeyError:
                    return abort(400)
                device_reading = DeviceReading(device=device.id, core_id=device.core_id, reading_mm=reading_mm, reading_reported=reading_reported)
                db.session.add(device_reading)
                db.session.commit()
                return jsonify(success=True)
            return abort(400)
        return abort(401)
    return redirect('/')

