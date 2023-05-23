from flask import Flask
from flask_restful import Api

from app.database import db
from app.extensions import migrate, marshmallow
from app.private import private_bp

def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(settings_module)

    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)
    Api(app)

    # blueprints
    app.register_blueprint(private_bp)

    return app
