import os
from celery import Celery
from flask import Flask, render_template, request, session, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(Config)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    db.init_app(app)
    import iot.models
    migrate = Migrate(app, db)
    celery.conf.update(app.config)

    # a simple page that says hello
    from iot.forms import SubscribeForm
    @app.route('/')
    def index():
        form = SubscribeForm()
        return render_template('index.html', form=form)
    from . import make_sub, api_bp, notify
    app.register_blueprint(make_sub.bp)
    app.register_blueprint(api_bp.bp)
    app.register_blueprint(notify.bp)
    return app