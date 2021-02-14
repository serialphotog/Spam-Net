from flask import Flask
from flask_security import Security, SQLAlchemySessionUserDatastore

from spam_net.config import get_config
from spam_net.database import db, init_db

from spam_net.models.user import User
from spam_net.models.roles import Role

def create_app(config_name):
    app = Flask("Spam Net")
    app.config.from_object(get_config(config_name))

    # Setup the database
    init_db(app)

    # Set up flask security
    user_datastore = SQLAlchemySessionUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    
    # Routes
    from spam_net.frontend.routes import frontend_bp
    app.register_blueprint(frontend_bp)

    return app
