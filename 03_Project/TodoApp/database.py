from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test1234!@localhost/TodoApplicationDatabase"
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:test1234!@localhost:3306/TodoApplicationDatabase"
SQLALCHEMY_DATABASE_URL = "postgresql://codingwithrobydb_user:GxoGn1Ngri3DPFbd6mWiqP7Y0txP6k71@dpg-ct2dotl6l47c73bae4v0-a.oregon-postgres.render.com/codingwithrobydb"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     connect_args={
#         "check_same_thread": False
#     }
# )  

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)  

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

