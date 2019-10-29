# Flood Tracker App

<img src='https://i.imgur.com/iiBFOY0.png' height='400px' />

A big problem in Miami is flooding. Code for Miami started an IOT project to build flood trackers. In this project we look into notifying end-users about flooding using Python.

See it running: http://secret-island-98010.herokuapp.com/  

## Features

* Subscribe to device to get alerts via SMS
* Receive post requests for /api/reading_request for particle readings - in development
* Display list of devices at /api/devices 
* display device reading by ID at /api/devices/<int:device_id>

## Requirements

* Docker and Docker Compose  
* Built on Python / Flask / Postres SQL


## To run this project:
Clone the project  
Create a folder with the name 'env' in the root directory of the repo and add a web-var.env file with values within that folder for the following:  
FLASK_APP=iot  
FLASK_ENV=development  
DATABASE_URL=postgresql://postgres@db/iot  
SECRET_KEY=secret_key  
TWILIO_ACCOUNT_ID=secret_key  
TWILIO_SECRET_KEY=secret_key  
TWILIO_VERIFY_SECRET_KEY=secret_key  
SQLALCHEMY_DATABASE_URI=secret_key  
PARTICLE_SECRET_KEY=secret_key  

run  
`docker-compose build && docker-compose up`  
navigate to localhost:8000

## NOTE
the dummy_data folder contains CSV's that you can import into the postgres container iot database
device_export is for the device table, device_readings_export is for the device readings table.

## Get Involved

* Join CFM Slack --> http://cfm-invite.herokuapp.com
* Go to the slack channel --> '#iotresiliency'

