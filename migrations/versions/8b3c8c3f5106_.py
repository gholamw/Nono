"""empty message

Revision ID: 8b3c8c3f5106
Revises: f39b74c0df65
Create Date: 2021-01-09 11:53:43.393900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b3c8c3f5106'
down_revision = 'f39b74c0df65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'crtransaction', 'customer', ['customer_id'], ['id'])
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
    op.drop_constraint(None, 'crtransaction', type_='foreignkey')
    # ### end Alembic commands ###
