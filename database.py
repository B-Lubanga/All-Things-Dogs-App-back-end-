from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///dog_adoption.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

def db_session():
    return Session()

def create_tables():
    from models.dog import Dog
    from models.owner import Owner
    from models.vet import Vet
    from models.rescue_center import RescueCenter
    from models.appointment import Appointment 

    # from models.database import Base

# Create all tables
    Base.metadata.create_all(engine)