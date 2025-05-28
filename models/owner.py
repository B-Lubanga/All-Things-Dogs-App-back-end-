from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(String)

    dog = relationship('Dog', back_populates='owner', uselist=False)
