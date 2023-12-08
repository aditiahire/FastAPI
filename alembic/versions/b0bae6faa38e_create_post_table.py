"""create post table

Revision ID: b0bae6faa38e
Revises: 
Create Date: 2023-12-06 10:17:45.056613

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0bae6faa38e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('post' , sa.Column('id' , sa.Integer(), nullable=False, primary_key=True), sa.Column('title' , sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
