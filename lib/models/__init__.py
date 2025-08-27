# lib/models/__init__.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define base class for models
Base = declarative_base()

# Create SQLite database
engine = create_engine("sqlite:///inventory.db")

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Import models so SQLAlchemy knows them before creating tables
from .item import Item

# Create tables if they don’t exist
Base.metadata.create_all(engine)
