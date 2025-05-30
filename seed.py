from database import create_tables, session, Base, engine
from models.dog import Dog
from models.owner import Owner
from models.vet import Vet
from models.rescue_center import RescueCenter
from models.appointment import Appointment
from datetime import datetime


#Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Sample entries(add your seed data)
owner1 = Owner(name="Jane Doe", contact="0700123456")
vet1 = Vet(name="Dr. Smith", clinic="Happy Paws Vet", contact="0734567890")
rescue1 = RescueCenter(name="Hope Rescue", location="Nairobi", contact="0711122233")

dog1 = Dog(name="Bruno", breed="German Shepherd", age=3, gender="Male",
           status="adoptable", location="Kisumu", owner=owner1, vet=vet1, rescue_center=rescue1)
appt1 = Appointment(date=datetime(2025, 6, 10, 10, 30),reason="Annual vaccination",dog=dog1,vet=vet1)

session.add_all([owner1, vet1, rescue1, dog1])
session.commit()
print("Database seeded!")
