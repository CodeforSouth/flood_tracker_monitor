from iot import db
import enum

class ContactMethod(enum.Enum):
    sms = 1
    phone = 2
    both = 3

class Device(db.Model):
    id = db.Column(db.Numeric, primary_key=True)
    longatuide = db.Column(db.Float, primary_key=False)
    latitude = db.Column(db.Float, primary_key=False)
    name = db.Column(db.String(40), primary_key=False)

    @property
    def serialize(self):
        return {'id': int(self.id), 'longatuide': self.longatuide, 'latitude': self.latitude, 'name': self.name}

class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zip_code = db.Column(db.Integer(), index=False, unique=False)
    phone_number = db.Column(db.BigInteger(), index=True, unique=True, nullable=False)
    device = db.Column(db.ForeignKey('device.id'), index=False, unique=False, nullable=False)
    verified = db.Column(db.Boolean(), index=False, unique=False)
    opted_out = db.Column(db.Boolean(), index=False, unique=False)
    last_contacted = db.Column(db.TIMESTAMP(timezone=False), index=False, unique=False)
    contact_method = db.Column(db.Enum(ContactMethod, name='contact_method'), index=False, nullable=False)
    

    def __repr__(self):
        return '<Phone Number {}>'.format(self.phone_number)  