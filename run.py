import click
import os

from spam_net import create_app, db
from spam_net.models.user import User
from spam_net.models.roles import Role, RolesUsers

app = create_app(os.getenv("FLASK_ENV", "development"))

@app.shell_context_processor
def shell():
    return {"db": db, "role": Role, "rolesusers": RolesUsers, "user": User}

# Add user command
@app.cli.command("add-user", short_help="Adds a new user to the system.")
@click.argument("email")
@click.password_option(help="Do not set a password on the command line!")
def add_user(email, password):
    """
    Adds a new user to the system.

    Args:
        email: The user's email address
        password: The password for the user
    """
    if User.find_by_email(email):
        error = f"Error: {email} is already registered."
        click.secho(f"{error}\n", fg="red", bold=True)
        return 1

    new_user = User(email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    message = f"Successfully added a new user: {new_user}"
    click.secho(message, fg="blue", bold=True)
    return 0
