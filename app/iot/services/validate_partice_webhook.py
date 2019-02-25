from flask import current_app as app

def get_particle_api_key():
    print(app.config)
    particle_key = app.config['PARTICLE_SECRET_KEY']
    return particle_key

def request_is_from_particle(request):
    body = request.get_json()
    return body['api_key'] == get_particle_api_key()
