from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, RadioField
from wtforms.fields.html5 import TelField
from wtforms.validators import DataRequired, Length

class SubscribeForm(FlaskForm):
    phone_number = TelField('Phone Number', validators=[DataRequired()])
    zip_code = IntegerField('Zip Code')
    device = RadioField(u'Device Subscription', validators=[DataRequired()], choices=[('1', 'Spring Park'), ('2', 'City Hall'), ('3', 'Surfside Park')])
    contact_method = RadioField(u'Contact Method', validators=[DataRequired()], choices=[('sms', 'SMS'), ('phone', 'Phone Call'), ('both', 'Both')])
    submit = SubmitField('Submit')

class VerifySubscribeForm(FlaskForm):
    verification_code = IntegerField('Verification Code', validators=[DataRequired()])
    submit = SubmitField('Submit')