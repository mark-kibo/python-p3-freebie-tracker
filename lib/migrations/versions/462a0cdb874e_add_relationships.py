"""Add relationships

Revision ID: 462a0cdb874e
Revises: 7a78e9f9fd4a
Create Date: 2023-09-30 11:20:40.464985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '462a0cdb874e'
down_revision = '7a78e9f9fd4a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freebies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dev', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('company', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_freebies_dev_devs'), 'devs', ['dev'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_freebies_company_companies'), 'companies', ['company'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freebies', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_freebies_company_companies'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_freebies_dev_devs'), type_='foreignkey')
        batch_op.drop_column('company')
        batch_op.drop_column('dev')

    # ### end Alembic commands ###
