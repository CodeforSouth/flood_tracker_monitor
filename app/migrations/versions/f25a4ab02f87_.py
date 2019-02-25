"""empty message

Revision ID: f25a4ab02f87
Revises: 31e529af20c1
Create Date: 2019-02-24 17:22:06.454150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f25a4ab02f87'
down_revision = '31e529af20c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscriber', sa.Column('date_created', sa.TIMESTAMP(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subscriber', 'date_created')
    # ### end Alembic commands ###
