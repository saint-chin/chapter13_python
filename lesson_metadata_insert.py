from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey, insert, select
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

# compiled = stmt.compile()
# print(str(compiled))  # the same as print(stmt)
# print(compiled.params)

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
insert_stmt = insert(address_table).returning(
    address_table.c.id, address_table.c.email_address)
with engine.connect() as conn:
    result = conn.execute(
        insert_stmt,
        [
            {"user_id": "1", "email_address": "spongebob@gmail.com"},
            {"user_id": "2", "email_address": "sandy@gmail.com"}
        ]
    )
    conn.commit()

select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
insert_stmt_2 = insert(address_table).from_select(
    ["user_id", "email_address"], select_stmt
).returning(
    address_table.c.user_id, address_table.c.email_address
)
with engine.connect() as conn:
    result = conn.execute(
        insert_stmt_2
    )
    rows = result.fetchall()
    conn.commit()

for row in rows:
    print(row)
