from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABSE_URL = 'sqlite:///./products.db'

engine = create_engine(SQLALCHEMY_DATABSE_URL, connect_args={'check_same_thread': False})

sessionlocal = sessionmaker(autoflush = False, autocommit = False, bind=engine)

SessionLocal = sessionlocal()

Base = declarative_base()
