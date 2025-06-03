from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Vet(Base):
    __tablename__ = 'vets'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    clinic = Column(String)
    contact = Column(String)
    location = Column(String)

    dogs = relationship('Dog', back_populates='vet')
    appointments = relationship('Appointment', back_populates='vet') 

    def __repr__(self):
        return f"<Vet(name={self.name}, location={self.location})>"