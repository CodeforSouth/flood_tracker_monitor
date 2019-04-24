# Flood tracker App:
heroku URL: http://secret-island-98010.herokuapp.com/
slack Channel: '#iotresiliency'
REQUIRES: Docker and Docker Compose

this is flask/postgresql app that currently allows users to do the following:
Subscribe to device alerts via sms
recive post requests for /api/reading_request for particle readings - in development
display list of devices at /api/devices
display device readings by id at /api/devices/<int:device_id>

## before begining please create a folder with the name 'env' in the root directory of the repo
## add a web-var.env file with values within that folder for the following:
FLASK_APP=iot
FLASK_ENV=development
DATABASE_URL=postgresql://postgres@db/iot
SECRET_KEY=secret_key
TWILIO_ACCOUNT_ID=secret_key
TWILIO_SECRET_KEY=secret_key
TWILIO_VERIFY_SECRET_KEY=secret_key
SQLALCHEMY_DATABASE_URI=secret_key
PARTICLE_SECRET_KEY=secret_key

To run this project:
Clone the project
run docker-compose build && docker-compose up
##NOTE
the dummy_data folder contains CSV's that you can import into the postgres container iot database
device_export is for the device table, device_readings_export is for the device readings table.
navigate to localhost:8000/

