"""User password hashing

Revision ID: 2a257644cb91
Revises: 4d656514843f
Create Date: 2021-02-14 13:21:37.879153

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2a257644cb91'
down_revision = '4d656514843f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=255), nullable=False))
    # ### end Alembic commands ###
