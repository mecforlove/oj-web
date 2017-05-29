"""empty message

Revision ID: 5c938b89edc2
Revises: b45572fab999
Create Date: 2017-05-19 23:26:33.941913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c938b89edc2'
down_revision = 'b45572fab999'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('commit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gmt_created', sa.DateTime(), server_default=sa.text(u'now()'), nullable=True),
    sa.Column('gmt_modified', sa.DateTime(), nullable=True),
    sa.Column('problem_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('detail', sa.String(length=512), nullable=True),
    sa.Column('language', sa.String(length=32), nullable=True),
    sa.Column('code', sa.Text(), nullable=True),
    sa.Column('mem', sa.Integer(), nullable=True),
    sa.Column('time', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['problem_id'], ['problem.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('commit')
    # ### end Alembic commands ###