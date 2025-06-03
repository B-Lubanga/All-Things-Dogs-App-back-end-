from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from database import session
from database import Base


class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(String)
    location = Column(String)

    # def __init__(self, name, contact, location):
    #     self.name = name
    #     self.contact = contact
    #     self.location = location

# # Function to add a new owner
# def add_owner(name, contact, location):
#     new_owner = Owner(name=name, contact=contact, location=location)
#     session.add(new_owner)
#     session.commit()
Owner.dogs = relationship('Dog', back_populates='owner')




