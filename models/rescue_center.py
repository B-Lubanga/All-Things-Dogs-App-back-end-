from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class RescueCenter(Base):
    __tablename__ = 'rescue_centers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    contact = Column(String)

    dogs = relationship('Dog', back_populates='rescue_center')
