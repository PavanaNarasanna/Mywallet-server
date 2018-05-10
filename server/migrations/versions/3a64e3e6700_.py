"""empty message

Revision ID: 3a64e3e6700
Revises: 47eabf3840e
Create Date: 2018-05-10 13:57:32.114960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a64e3e6700'
down_revision = '47eabf3840e'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categorys', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key('USER', 'categorys', 'users', ['user_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('USER', 'categorys', type_='foreignkey')
    op.drop_column('categorys', 'user_id')
    ### end Alembic commands ###
