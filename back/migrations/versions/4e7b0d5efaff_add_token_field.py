"""Add token field

Revision ID: 4e7b0d5efaff
Revises: c001ca2acf06
Create Date: 2022-05-01 20:49:04.764467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e7b0d5efaff'
down_revision = 'c001ca2acf06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('phonecode', sa.Column('code', sa.String(length=60), nullable=True))
    op.drop_column('phonecode', 'code_auth')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('phonecode', sa.Column('code_auth', sa.VARCHAR(length=60), autoincrement=False, nullable=True))
    op.drop_column('phonecode', 'code')
    # ### end Alembic commands ###
