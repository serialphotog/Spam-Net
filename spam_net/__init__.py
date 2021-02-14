from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from spam_net.config import get_config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    app = Flask("Spam Net")
    app.config.from_object(get_config(config_name))

    # Routes
    from spam_net.frontend.routes import frontend_bp
    app.register_blueprint(frontend_bp)

    # Set up the database
    db.init_app(app)
    migrate.init_app(app, db)

    return app
