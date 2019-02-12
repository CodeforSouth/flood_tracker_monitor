from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired

class SubscribeForm(FlaskForm):
    phone_number = IntegerField('Phone Number', validators=[DataRequired()])
    zip_code = IntegerField('Zip Code', validators=[])
    device = RadioField(u'Device Subscription', choices=[('1', '1'), ('2', '2'), ('3', '3')], validators=[DataRequired()])
    contact_method = RadioField(u'Contact Method', choices=[('1', 'SMS'), ('2', 'Phone Call'), ('3', 'Both')], validators=[DataRequired()])
    submit = SubmitField('Submit')