"""empty message

Revision ID: bad873767e20
Revises: 
Create Date: 2022-03-09 09:34:56.105965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bad873767e20'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=150), nullable=True),
    sa.Column('postcode', sa.String(length=6), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id_from', sa.Integer(), nullable=True),
    sa.Column('user_id_to', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('text', sa.String(length=300), nullable=True),
    sa.ForeignKeyConstraint(['user_id_from'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id_to'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message')
    op.drop_table('user')
    # ### end Alembic commands ###