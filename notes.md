## how to delete a directory with everything inside
rm -rf directory_name

## DBAPI
DBAPI is shorthand for the phrase “Python Database API Specification”. This is a widely used specification within Python to define common usage patterns for all database connection packages. The DBAPI is a “low level” API which is typically the lowest level system used in a Python application to talk to a database. SQLAlchemy’s dialect system is constructed around the operation of the DBAPI, providing individual dialect classes which service a specific DBAPI on top of a specific database engine; for example, the create_engine() URL postgresql+psycopg2://@localhost/test refers to the psycopg2 DBAPI/dialect combination, whereas the URL mysql+mysqldb://@localhost/test refers to the MySQL for Python DBAPI/dialect combination.

## commiting data
The transaction is not committed automatically; if we want to commit data we need to call Connection.commit() as we’ll see in the next section.