import databases
from sqlalchemy import create_engine, MetaData

SQLALCHEMY_DATABASE_URL = "postgresql://root:password@database/example"

database = databases.Database(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

metadata = MetaData()