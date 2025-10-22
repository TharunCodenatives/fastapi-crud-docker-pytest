import os
from sqlalchemy import Column, DateTime, Integer, String, Table, func
from sqlalchemy.sql import func as sql_func  # or use already imported func
from sqlalchemy import MetaData, create_engine
from databases import Database

#DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

engine = create_engine(DATABASE_URL)
metadata = MetaData()

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=sql_func.now(), nullable=False),
)

database = Database(DATABASE_URL)


# Docker Code
# import os
# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, func
# from databases import Database

# DATABASE_URL = os.getenv("DATABASE_URL")

# engine = create_engine(DATABASE_URL)
# metadata = MetaData()

# notes = Table(
#     "notes",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("title", String(50)),
#     Column("description", String(50)),
#     Column("created_date", DateTime, default=func.now(), nullable=False),
# )

# database = Database(DATABASE_URL)
