"""empty message

Revision ID: d5ef342bd5f3
Revises: 341109fb89be
Create Date: 2020-12-01 16:25:02.330166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5ef342bd5f3'
down_revision = '341109fb89be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('description', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_account_description'), 'account', ['description'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_account_description'), table_name='account')
    op.drop_column('account', 'description')
    # ### end Alembic commands ###
