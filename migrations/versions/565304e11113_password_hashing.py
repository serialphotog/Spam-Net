"""Password hashing

Revision ID: 565304e11113
Revises: 2a257644cb91
Create Date: 2021-02-14 13:25:16.266057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '565304e11113'
down_revision = '2a257644cb91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###
