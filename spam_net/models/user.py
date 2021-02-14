# A simple user model for the Spam Net system
from flask_security import UserMixin

from sqlalchemy.orm import relationship, backref

from spam_net import db

class User(db.Model, UserMixin):
    """
    Represents a user.
    """

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary='roles_users',
        backref = db.backref('users', lazy='dynamic'))

    def __repr__(self):
        """
        Returns a string representation of this user.
        """
        return(
            f"<User email={self.email} id={self.id}, roles={self.roles}>"
        )
