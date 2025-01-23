from sqlalchemy import Column, Integer, String, Text, ForeignKey, Decimal
from sqlalchemy.orm import relationship
from db_setup import Base

class Category(Base):
    __tablename__ = "categories"
    
    id_category = Column(Integer, primary_key=True, index=True)
    description = Column(String(100), nullable=False)

    # Relationship with restaurants
    restaurants = relationship("Restaurant", back_populates="category")

class Location(Base):
    __tablename__ = "locations"
    
    id_location = Column(Integer, primary_key=True, index=True)
    city = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)

    # Relationship with restaurants
    restaurants = relationship("Restaurant", back_populates="location")

class Restaurant(Base):
    __tablename__ = "restaurants"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    address = Column(Text, nullable=False)
    price = Column(String(50))
    rating = Column(Decimal(2, 1))
    cuisine_type = Column(String(100))
    latitude = Column(Decimal(10, 6))
    longitude = Column(Decimal(10, 6))
    
    # Relationships with other tables
    id_category = Column(Integer, ForeignKey("categories.id_category"))
    id_location = Column(Integer, ForeignKey("locations.id_location"))
    
    category = relationship("Category", back_populates="restaurants")
    location = relationship("Location", back_populates="restaurants")
