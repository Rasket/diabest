import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID
from .phonecode import phonecode_table


metadata = sqlalchemy.MetaData()


card_table = sqlalchemy.Table(
    "card",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("photo", sqlalchemy.String(255), unique=False),
    sqlalchemy.Column("description", sqlalchemy.String(240), unique=False),
    sqlalchemy.Column("name", sqlalchemy.String(40), unique=False),
    sqlalchemy.Column("creator", sqlalchemy.ForeignKey(phonecode_table.c.phone)),
)
