from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime

from database import Base

from .dog import Dog
from .vet import Vet  

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    reason = Column(String, nullable=True)

    dog_id = Column(Integer, ForeignKey('dogs.id'), nullable=False)
    vet_id = Column(Integer, ForeignKey('vets.id'), nullable=False)

    dog = relationship("Dog", back_populates="appointments")
    vet = relationship("Vet", back_populates="appointments")

    def __repr__(self):
        return f"<Appointment Dog='{self.dog.name}' Vet='{self.vet.name}' Date='{self.date.strftime('%Y-%m-%d %H:%M')}' Reason='{self.reason}'>"