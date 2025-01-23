from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date, DateTime, func
from sqlalchemy.orm import relationship
from db_setup import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())

    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    status = Column(String(20), default="pending")
    due_date = Column(Date)
    created_at = Column(DateTime, default=func.now())

    user = relationship("User", back_populates="tasks")
