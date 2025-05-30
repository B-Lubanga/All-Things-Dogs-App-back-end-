from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database import Base

Base = declarative_base()

class RescueCenter(Base):
    __tablename__ = 'rescue_centers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    contact = Column(String)

    dogs = relationship('Dog', back_populates='rescue_center')
