# Models for user roles
from flask_security import RoleMixin

from sqlalchemy import ForeignKey

from spam_net import db

class RolesUsers(db.Model):
    __table_name__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer(), ForeignKey('role.id'))

class Role(db.Model, RoleMixin):
    __table__name__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
