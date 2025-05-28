from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)
    age = Column(Integer)
    gender = Column(String)
    status = Column(String)  # adoptable, rescued, for sale
    location = Column(String)

    owner_id = Column(Integer, ForeignKey('owners.id'))
    vet_id = Column(Integer, ForeignKey('vets.id'))
    rescue_center_id = Column(Integer, ForeignKey('rescue_centers.id'))

    owner = relationship('Owner', back_populates='dog')
    vet = relationship('Vet', back_populates='dogs')
    rescue_center = relationship('RescueCenter', back_populates='dogs')
    appointments = relationship('Appointment', back_populates='dog')

