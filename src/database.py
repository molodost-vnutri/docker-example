from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://root:password@database/example"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

database = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(bind=engine)