from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.dog import Dog
from models.owner import Owner
from models.vet import Vet
from models.rescue_center import RescueCenter
from models.appointment import Appointment 


engine = create_engine("sqlite:///dog_adoption.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
