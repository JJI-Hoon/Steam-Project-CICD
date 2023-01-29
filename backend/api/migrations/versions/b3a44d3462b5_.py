"""empty message

Revision ID: b3a44d3462b5
Revises: 82f234675d71
Create Date: 2023-01-29 10:09:53.220111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3a44d3462b5'
down_revision = '82f234675d71'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('history', 'userid',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('history', 'gameid',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_index('ix_history_id', table_name='history')
    op.drop_column('history', 'id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('history', sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False))
    op.create_index('ix_history_id', 'history', ['id'], unique=False)
    op.alter_column('history', 'gameid',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('history', 'userid',
               existing_type=sa.BIGINT(),
               nullable=True)
    # ### end Alembic commands ###
