"""empty message

Revision ID: 889ff2995f88
Revises: 847678b885e3
Create Date: 2020-12-21 21:53:43.622595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '889ff2995f88'
down_revision = '847678b885e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('bulk_bulk_expense', sa.Float(), nullable=True))
    op.add_column('products', sa.Column('bulk_expense', sa.Float(), nullable=True))
    op.add_column('products', sa.Column('single_expense', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'single_expense')
    op.drop_column('products', 'bulk_expense')
    op.drop_column('products', 'bulk_bulk_expense')
    # ### end Alembic commands ###
