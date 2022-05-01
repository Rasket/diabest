import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID

metadata = sqlalchemy.MetaData()


phonecode_table = sqlalchemy.Table(
    "phonecode",
    metadata,
    sqlalchemy.Column("phone", sqlalchemy.String(12), primary_key=True),
    sqlalchemy.Column("code", sqlalchemy.String(60), unique=False),
    sqlalchemy.Column("token", sqlalchemy.String(20), unique=False),
    sqlalchemy.Column("expr_date", sqlalchemy.DateTime(), unique=False)
)
