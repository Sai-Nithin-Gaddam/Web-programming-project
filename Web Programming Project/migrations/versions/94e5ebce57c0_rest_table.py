"""rest table

Revision ID: 94e5ebce57c0
Revises: 4f463d6ee5ba
Create Date: 2022-08-03 12:36:38.804799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94e5ebce57c0'
down_revision = '4f463d6ee5ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('res_name', sa.String(length=140), nullable=True),
    sa.Column('res_Address', sa.String(length=140), nullable=True),
    sa.Column('res_Cusine', sa.String(length=140), nullable=True),
    sa.Column('res_Rating', sa.String(length=140), nullable=True),
    sa.Column('area_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['area_id'], ['area.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rest')
    # ### end Alembic commands ###