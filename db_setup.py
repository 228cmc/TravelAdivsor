from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DATABASE_URI

# Set up the database connection
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class for all models
Base = declarative_base()

def init_db():
    """
    Initialize the database tables.

    Note: Models (Category, Location, Restaurant) must be imported here 
    to avoid circular import issues. This ensures they are registered 
    in Base.metadata and can be used to create the tables.
    """
    from models import Category, Location, Restaurant  # Import models here
    Base.metadata.create_all(bind=engine)  # Create all tables if they don't exist
