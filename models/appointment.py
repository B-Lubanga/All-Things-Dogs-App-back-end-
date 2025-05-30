from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime

from .dog import Dog
from .vet import Vet  

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    reason = Column(String)

    dog_id = Column(Integer, ForeignKey('dogs.id'))
    vet_id = Column(Integer, ForeignKey('vets.id'))

    dog = relationship(Dog, back_populates='appointments')
    vet = relationship(Vet, back_populates='appointments')
