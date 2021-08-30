"""

Initial Alembic migration with all syft tables

Revision ID: 0cda31d54345
Revises:
Create Date: 2021-08-29 20:11:00.622963

"""
# third party
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0cda31d54345"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "association",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("date", sa.DateTime(), nullable=True),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("address", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "association_request",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("requested_date", sa.String(length=255), nullable=True),
        sa.Column("accepted_date", sa.String(length=255), nullable=True),
        sa.Column("address", sa.String(length=255), nullable=True),
        sa.Column("node", sa.String(length=255), nullable=True),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("reason", sa.String(length=255), nullable=True),
        sa.Column("status", sa.String(length=255), nullable=True),
        sa.Column("source", sa.LargeBinary(length=4096), nullable=True),
        sa.Column("target", sa.LargeBinary(length=4096), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "bin_object",
        sa.Column("id", sa.String(length=256), nullable=False),
        sa.Column("binary", sa.LargeBinary(length=3072), nullable=True),
        sa.Column("obj_name", sa.String(length=3072), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "dataset",
        sa.Column("id", sa.String(length=256), nullable=False),
        sa.Column("name", sa.String(length=256), nullable=True),
        sa.Column("manifest", sa.String(length=2048), nullable=True),
        sa.Column("description", sa.String(length=2048), nullable=True),
        sa.Column("tags", sa.JSON(), nullable=True),
        sa.Column("str_metadata", sa.JSON(), nullable=True),
        sa.Column("blob_metadata", sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "environment",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("state", sa.Integer(), nullable=True),
        sa.Column("provider", sa.String(length=255), nullable=True),
        sa.Column("region", sa.String(length=255), nullable=True),
        sa.Column("instance_type", sa.String(length=255), nullable=True),
        sa.Column("address", sa.String(length=255), nullable=True),
        sa.Column("syft_address", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("destroyed_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "group",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "role",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("can_triage_requests", sa.Boolean(), nullable=True),
        sa.Column("can_edit_settings", sa.Boolean(), nullable=True),
        sa.Column("can_create_users", sa.Boolean(), nullable=True),
        sa.Column("can_create_groups", sa.Boolean(), nullable=True),
        sa.Column("can_edit_roles", sa.Boolean(), nullable=True),
        sa.Column("can_manage_infrastructure", sa.Boolean(), nullable=True),
        sa.Column("can_upload_data", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "setup",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("domain_name", sa.String(length=255), nullable=True),
        sa.Column("node_id", sa.String(length=32), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "bin_obj_dataset",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(length=256), nullable=True),
        sa.Column("obj", sa.String(length=256), nullable=True),
        sa.Column("dataset", sa.String(length=256), nullable=True),
        sa.Column("dtype", sa.String(length=256), nullable=True),
        sa.Column("shape", sa.String(length=256), nullable=True),
        sa.ForeignKeyConstraint(["dataset"], ["dataset.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["obj"], ["bin_object.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "obj_metadata",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("obj", sa.String(length=256), nullable=True),
        sa.Column("tags", sa.JSON(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("read_permissions", sa.JSON(), nullable=True),
        sa.Column("search_permissions", sa.JSON(), nullable=True),
        sa.ForeignKeyConstraint(["obj"], ["bin_object.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "syft_user",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("hashed_password", sa.String(length=512), nullable=True),
        sa.Column("salt", sa.String(length=255), nullable=True),
        sa.Column("private_key", sa.String(length=2048), nullable=True),
        sa.Column("verify_key", sa.String(length=2048), nullable=True),
        sa.Column("role", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["role"],
            ["role.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "request",
        sa.Column("id", sa.String(length=255), nullable=False),
        sa.Column("date", sa.DateTime(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("user_name", sa.String(length=255), nullable=True),
        sa.Column("object_id", sa.String(length=255), nullable=True),
        sa.Column("reason", sa.String(length=255), nullable=True),
        sa.Column("status", sa.String(length=255), nullable=True),
        sa.Column("request_type", sa.String(length=255), nullable=True),
        sa.Column("verify_key", sa.String(length=255), nullable=True),
        sa.Column("object_type", sa.String(length=255), nullable=True),
        sa.Column("tags", sa.JSON(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["syft_user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "userenvironment",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user", sa.Integer(), nullable=True),
        sa.Column("environment", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["environment"],
            ["environment.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user"],
            ["syft_user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "usergroup",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user", sa.Integer(), nullable=True),
        sa.Column("group", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["group"],
            ["group.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user"],
            ["syft_user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("usergroup")
    op.drop_table("userenvironment")
    op.drop_table("request")
    op.drop_table("syft_user")
    op.drop_table("obj_metadata")
    op.drop_table("bin_obj_dataset")
    op.drop_table("setup")
    op.drop_table("role")
    op.drop_table("group")
    op.drop_table("environment")
    op.drop_table("dataset")
    op.drop_table("bin_object")
    op.drop_table("association_request")
    op.drop_table("association")
    # ### end Alembic commands ###
