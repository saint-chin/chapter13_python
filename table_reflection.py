# You already have a table in the database and want to query it without explicitly defining columns in Python.
from sqlalchemy import create_engine, MetaData, Table, select
# Connect to the db
engine = create_engine("sqlite:///books_authors.db")
metadata_obj = MetaData()

# Reflect the table
some_table = Table("books", metadata_obj, autoload_with=engine)

# Query the table
with engine.connect() as conn:
    result = conn.execute(select(some_table))
    for row in result:
        print(row)
