import databases
import sqlalchemy
from credential import db_info

DATABASE_URL = db_info["DATABASE_URL"]
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData(schema="public")
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
