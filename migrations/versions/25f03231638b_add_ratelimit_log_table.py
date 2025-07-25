"""add_ratelimit_log_table

Revision ID: 25f03231638b
Revises: ee132f190ac7
Create Date: 2025-07-08 11:57:29.921750

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '25f03231638b'
down_revision: Union[str, None] = 'ee132f190ac7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ratelimitlog',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('ip_address', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=True),
    sa.Column('endpoint', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('request_count', sa.Integer(), nullable=False),
    sa.Column('request_method', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('request_path', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('window_start', postgresql.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('window_end', postgresql.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('blocked_until', postgresql.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ratelimitlog_ip_address'), 'ratelimitlog', ['ip_address'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ratelimitlog_ip_address'), table_name='ratelimitlog')
    op.drop_table('ratelimitlog')
    # ### end Alembic commands ###
