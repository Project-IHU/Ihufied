"""empty message

Revision ID: 513c6831925d
Revises: 937168e359f3
Create Date: 2020-08-27 13:32:51.714866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '513c6831925d'
down_revision = '937168e359f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('faculty',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('faculty_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['faculty_id'], ['faculty.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=30), nullable=True),
    sa.Column('lastname', sa.String(length=30), nullable=True),
    sa.Column('middlename', sa.String(length=30), nullable=True),
    sa.Column('regnumber', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('image_name', sa.String(length=50), nullable=True),
    sa.Column('level', sa.String(length=3), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('user_status', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['department_id'], ['department.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('regnumber')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('department')
    op.drop_table('faculty')
    # ### end Alembic commands ###
