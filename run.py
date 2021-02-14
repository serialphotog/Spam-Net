import click
import os

from spam_net import create_app, db
from spam_net.models.user import User
from spam_net.models.roles import Role, RolesUsers

app = create_app(os.getenv("FLASK_ENV", "development"))

@app.shell_context_processor
def shell():
    return {"db": db, "role": Role, "rolesusers": RolesUsers, "User": User}
