"""
Create the database connection.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.settings import Settings

# Instantiate the settings.
settings = Settings()

# Define the database connection.
SQLALCHEMY_DATABASE_URL = settings.get_database_uri()

# Create the engine using the database URI.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
# Create the Session
SessionLocal = sessionmaker(bind=engine)

# Define the Base as declarative, to be used in the contact.py file.
Base = declarative_base()
