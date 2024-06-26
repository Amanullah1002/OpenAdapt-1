"""remove_recording_timestamp_fks

Revision ID: 87a78a84a8bf
Revises: f9586c10a561
Create Date: 2024-04-24 20:16:31.970666

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "87a78a84a8bf"
down_revision = "f9586c10a561"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("action_event", schema=None) as batch_op:
        batch_op.drop_constraint(
            "fk_input_event_recording_timestamp_recording", type_="foreignkey"
        )
        batch_op.drop_constraint(
            "fk_input_event_window_event_timestamp_window_event", type_="foreignkey"
        )
        batch_op.drop_constraint(
            "fk_input_event_screenshot_timestamp_screenshot", type_="foreignkey"
        )

    with op.batch_alter_table("screenshot", schema=None) as batch_op:
        batch_op.drop_constraint(
            "fk_screenshot_recording_timestamp_recording", type_="foreignkey"
        )

    with op.batch_alter_table("window_event", schema=None) as batch_op:
        batch_op.drop_constraint(
            "fk_window_event_recording_timestamp_recording", type_="foreignkey"
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("window_event", schema=None) as batch_op:
        batch_op.create_foreign_key(
            "fk_window_event_recording_timestamp_recording",
            "recording",
            ["recording_timestamp"],
            ["timestamp"],
        )

    with op.batch_alter_table("screenshot", schema=None) as batch_op:
        batch_op.create_foreign_key(
            "fk_screenshot_recording_timestamp_recording",
            "recording",
            ["recording_timestamp"],
            ["timestamp"],
        )

    with op.batch_alter_table("action_event", schema=None) as batch_op:
        batch_op.create_foreign_key(
            "fk_input_event_screenshot_timestamp_screenshot",
            "screenshot",
            ["screenshot_timestamp"],
            ["timestamp"],
        )
        batch_op.create_foreign_key(
            "fk_input_event_window_event_timestamp_window_event",
            "window_event",
            ["window_event_timestamp"],
            ["timestamp"],
        )
        batch_op.create_foreign_key(
            "fk_input_event_recording_timestamp_recording",
            "recording",
            ["recording_timestamp"],
            ["timestamp"],
        )

    # ### end Alembic commands ###
