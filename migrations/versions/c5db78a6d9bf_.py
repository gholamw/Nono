"""empty message

Revision ID: c5db78a6d9bf
Revises: 6e50aacf172b
Create Date: 2021-01-09 11:56:41.809719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5db78a6d9bf'
down_revision = '6e50aacf172b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('crtransaction', 'customer_id')
    op.add_column('customer', sa.Column('remaining_balance', sa.Float(), nullable=True))
    op.add_column('drtransaction', sa.Column('customer_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'drtransaction', 'customer', ['customer_id'], ['id'])
    op.drop_constraint(None, 'revtransaction', type_='foreignkey')
    op.drop_column('revtransaction', 'customer_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('revtransaction', sa.Column('customer_id', sa.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'revtransaction', 'customer', ['customer_id'], ['id'])
    op.drop_constraint(None, 'drtransaction', type_='foreignkey')
    op.drop_column('drtransaction', 'customer_id')
    op.drop_column('customer', 'remaining_balance')
    op.add_column('crtransaction', sa.Column('customer_id', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###
