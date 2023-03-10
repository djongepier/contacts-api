"""Add phone number1

Revision ID: ad70f08621f5
Revises: 72a62da8d4bb
Create Date: 2023-01-13 11:56:18.774367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad70f08621f5'
down_revision = '72a62da8d4bb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('phone_number', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contacts', 'phone_number')
    # ### end Alembic commands ###
