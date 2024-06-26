"""Add png_diff_data and png_diff_mask_data

Revision ID: 8713b142f5de
Revises: 607d1380b5ae
Create Date: 2023-07-09 15:31:28.462388

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "8713b142f5de"
down_revision = "607d1380b5ae"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("screenshot", schema=None) as batch_op:
        batch_op.add_column(sa.Column("png_diff_data", sa.LargeBinary(), nullable=True))
        batch_op.add_column(
            sa.Column("png_diff_mask_data", sa.LargeBinary(), nullable=True)
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("screenshot", schema=None) as batch_op:
        batch_op.drop_column("png_diff_mask_data")
        batch_op.drop_column("png_diff_data")

    # ### end Alembic commands ###
