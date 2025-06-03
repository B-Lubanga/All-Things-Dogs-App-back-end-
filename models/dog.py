from sqlalchemy.orm import relationship
from database import Base,create_tables
from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()


from models.rescue_center import RescueCenter  


class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)
    age = Column(String)
    gender = Column(String)
    purpose = Column(String) # adoption, rescued, sale 
    location = Column(String)

    owner_id = Column(Integer, ForeignKey('owners.id'),nullable=False)
    vet_id = Column(Integer, ForeignKey('vets.id'))  
    rescue_center_id = Column(Integer, ForeignKey('rescue_centers.id')) 

    owner = relationship('Owner', back_populates='dogs')
    vet = relationship('Vet', back_populates='dogs')
    rescue_center = relationship('RescueCenter', back_populates='dogs', lazy='joined')
    appointments = relationship('Appointment', back_populates='dog')

