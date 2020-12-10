import os

PG_USER = "user"
PG_PASSWORD = os.environ.get("PG_PASSWORD", "")
PG_HOST = os.environ.get("PG_HOST", "database")
PG_PORT = "5432"
PG_DB = "my_shop"


SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
