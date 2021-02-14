# A simple user model for the Spam Net system
from flask_security import UserMixin
from flask_security.utils import hash_password

from sqlalchemy.orm import relationship, backref

from spam_net import db

class User(db.Model, UserMixin):
    """
    Represents a user.
    """

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
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

    @property
    def password(self):
        """
        Ensure there is no accessor for the password.
        """
        raise AttributeError("Password: Write-Only field")

    @password.setter
    def password(self, password):
        """
        Sets the password for the user.
        """
        self.password_hash = hash_password(password)

    @classmethod
    def find_by_email(cls, email):
        """
        Searches for a user based on an email address.
        """
        return cls.query.filter_by(email=email).first()
