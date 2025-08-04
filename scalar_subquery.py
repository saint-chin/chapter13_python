from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey, insert, select, bindparam
# Always declare engine!
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
# Metadata is a container that stores table definitions
metadata_obj = MetaData()
# user_table is a table definition, not a real table in the db
user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String)
)

address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False),
)

metadata_obj.create_all(engine)
# Selects user_id from user_table where name is "username", which is a placeholder
scalar_subq = (
    select(user_table.c.id)
    .where(user_table.c.name == bindparam("username"))
    .scalar_subquery()
)

with engine.connect() as conn:
    result = conn.execute(
        insert(user_table),
        [
            {"name": "spongebob", "fullname": "Spongebob Squarepants"},
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patrick", "fullname": "Patrick Star"},
        ],
    )
    conn.commit()
# Takes an id of "spongebob" and inserts it into address_table as well as email_address
with engine.connect() as conn:
    result = conn.execute(
        insert(address_table).values(user_id=scalar_subq),
        [
            {
                "username": "spongebob",
                "email_address": "spongebob@sqlalchemy.org",
            },
            {
                "username": "sandy",
                "email_address": "sandy@sqlalchemy.org"
            },
            {
                "username": "sandy",
                "email_address": "sandy@squirrelpower.org"
            },
        ],
    )
    conn.commit()
