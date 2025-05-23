"""add_next_of_kin_table

Revision ID: 02f4d8d0f368
Revises: cfb125022096
Create Date: 2025-05-20 18:14:31.045656

"""

from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "02f4d8d0f368"
down_revision: Union[str, None] = "cfb125022096"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "nextofkin",
        sa.Column(
            "full_name", sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False
        ),
        sa.Column(
            "relationship",
            sa.Enum(
                "Spouse",
                "Parent",
                "Child",
                "Sibling",
                "Other",
                name="relationshiptypeenum",
            ),
            nullable=False,
        ),
        sa.Column("email", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("phone_number", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("address", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("city", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("country", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("nationality", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("id_number", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("passport_number", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("is_primary", sa.Boolean(), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("updated_at", postgresql.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("user_id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.alter_column(
        "profile",
        "title",
        existing_type=postgresql.ENUM("Mr", "Mrs", "Miss", name="salutationschema"),
        type_=postgresql.ENUM("Mr", "Mrs", "Miss", name="salutationenum"),
        existing_nullable=False,
    )
    op.alter_column(
        "profile",
        "gender",
        existing_type=postgresql.ENUM("Male", "Female", "Other", name="genderschema"),
        type_=postgresql.ENUM("Male", "Female", "Other", name="genderenum"),
        existing_nullable=False,
    )
    op.alter_column(
        "profile",
        "marital_status",
        existing_type=postgresql.ENUM(
            "Married", "Divorced", "Single", "Widowed", name="maritalstatusschema"
        ),
        type_=postgresql.ENUM(
            "Married", "Divorced", "Single", "Widowed", name="maritalstatusenum"
        ),
        existing_nullable=False,
    )
    op.alter_column(
        "profile",
        "means_of_identification",
        existing_type=postgresql.ENUM(
            "Passport",
            "Drivers_License",
            "National_ID",
            name="identificationtypeschema",
        ),
        type_=postgresql.ENUM(
            "Passport",
            "Drivers_License",
            "National_ID",
            name="identificationtypeenum",
        ),
        existing_nullable=False,
    )
    op.alter_column(
        "profile",
        "employment_status",
        existing_type=postgresql.ENUM(
            "Employed",
            "Unemployed",
            "Self_Employed",
            "Student",
            "Retired",
            name="employmentstatusschema",
        ),
        type_=postgresql.ENUM(
            "Employed",
            "Unemployed",
            "Self_Employed",
            "Student",
            "Retired",
            name="employmentstatusenum",
        ),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "profile",
        "employment_status",
        existing_type=postgresql.ENUM(
            "Employed",
            "Unemployed",
            "Self_Employed",
            "Student",
            "Retired",
            name="employmentstatusenum",
        ),
        type_=postgresql.ENUM(
            "Employed",
            "Unemployed",
            "Self_Employed",
            "Student",
            "Retired",
            name="employmentstatusschema",
        ),
        existing_nullable=False,
    )
    op.alter_column(
        "profile",
        "means_of_identification",
        existing_type=postgresql.ENUM(
            "Passport",
            "Drivers_License",
            "National_ID",
            name="identificationtypeenum",
        ),
        type_=postgresql.ENUM(
            "Passport",
            "Drivers_License",
            "National_ID",
            name="identificationtypeschema",
        ),
        existing_nullable=False,
    )
    op.alter_column(
        "profile",
        "marital_status",
        existing_type=postgresql.ENUM(
            "Married", "Divorced", "Single", "Widowed", name="maritalstatusenum"
        ),
        type_=postgresql.ENUM(
            "Married", "Divorced", "Single", "Widowed", name="maritalstatusschema"
        ),
        existing_nullable=False,
    )
    op.alter_column(
        "profile",
        "gender",
        existing_type=postgresql.ENUM("Male", "Female", "Other", name="genderenum"),
        type_=postgresql.ENUM("Male", "Female", "Other", name="genderschema"),
        existing_nullable=False,
    )
    op.alter_column(
        "profile",
        "title",
        existing_type=postgresql.ENUM("Mr", "Mrs", "Miss", name="salutationenum"),
        type_=postgresql.ENUM("Mr", "Mrs", "Miss", name="salutationschema"),
        existing_nullable=False,
    )
    op.drop_table("nextofkin")
    # ### end Alembic commands ###
