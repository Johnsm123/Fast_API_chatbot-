from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
<<<<<<< Updated upstream

# Database configuration
DATABASE_URL = "sqlite:///./intelligent_conversational_ai.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Database model
=======
import os
from dotenv import load_dotenv

from urllib.parse import quote_plus

# Load environment variables
load_dotenv()

# Database configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "Samsimi@123")
DB_NAME = os.getenv("DB_NAME", "intelligent_conversational_ai_db")

# URL encode the password to handle special characters
encoded_password = quote_plus(DB_PASSWORD)
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create engine
engine = create_engine(DATABASE_URL)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Student model for database
>>>>>>> Stashed changes
class ConversationalEntityDB(Base):
    __tablename__ = "conversational_entities"
    
    id = Column(Integer, primary_key=True, index=True)
<<<<<<< Updated upstream
    name = Column(String, index=True)
    age = Column(Integer)
    grade = Column(String)
=======
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    grade = Column(String(10), nullable=False)

# Create tables
def create_tables():
    Base.metadata.create_all(bind=engine)
>>>>>>> Stashed changes

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
<<<<<<< Updated upstream
        db.close()

# Create tables
def create_tables():
    Base.metadata.create_all(bind=engine)
=======
        db.close()
>>>>>>> Stashed changes
