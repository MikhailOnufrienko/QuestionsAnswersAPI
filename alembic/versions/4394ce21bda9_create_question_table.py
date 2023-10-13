"""Create question table.

Revision ID: 4394ce21bda9
Revises: 
Create Date: 2023-10-13 16:46:59.486017

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '4394ce21bda9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('CREATE SCHEMA q_a;')
    op.create_table('ques_and_ans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.Text(), nullable=True),
    sa.Column('answer', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('added_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    schema='q_a'
    )
    op.create_index(
        'index_ques_and_ans_id', 'ques_and_ans', ['id'],
        unique=True, schema='q_a', if_not_exists=True
    )


def downgrade() -> None:
    op.drop_table('ques_and_ans', schema='q_a')
