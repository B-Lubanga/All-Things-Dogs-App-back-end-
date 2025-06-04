from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

from database import Base


class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    location = Column(String, nullable=False)

    dogs = relationship("Dog", back_populates="owner", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Owner Name='{self.name}' Contact='{self.contact}' Location='{self.location}'>"
