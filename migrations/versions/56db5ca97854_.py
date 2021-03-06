"""empty message

Revision ID: 56db5ca97854
Revises: b72419c59f0b
Create Date: 2020-11-17 20:51:38.994456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56db5ca97854'
down_revision = 'b72419c59f0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('crtransaction', sa.Column('current_balance', sa.Float(), nullable=True))
    op.add_column('drtransaction', sa.Column('current_balance', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('drtransaction', 'current_balance')
    op.drop_column('crtransaction', 'current_balance')
    # ### end Alembic commands ###
