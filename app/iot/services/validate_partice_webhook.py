from flask import current_app as app

def get_particle_api_key():
    particle_key = app.config['PARTICLE_SECRET_KEY']
    return particle_key

def request_is_from_particle(request):
    args = request.args.to_dict()
    #TODO include default using get method.
    return args['key'] == get_particle_api_key()
