from database import create_tables, session, Base, engine
from models.dog import Dog
from models.owner import Owner
from models.vet import Vet
from models.rescue_center import RescueCenter
from models.appointment import Appointment
from datetime import datetime, timedelta


#Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Sample entries(add your seed data)
owner = [Owner(name="Jane Okoth", contact="0700123456", location= "Nairobi"),
        Owner(name="John Maina", contact="0700654321", location="Mombasa"),
        Owner(name="Alice Wambui", contact="0712345678", location="Kisumu"),
        Owner(name="Bob Ochieng'", contact="0723456789", location="Nakuru"),
        Owner(name="Charlie Agenga", contact="0734567890", location="Eldoret"),
        Owner(name="Diana Murua", contact="0745678901", location="Meru"),
        Owner(name="Ethan Kibet", contact="0756789012", location="Nairobi"),
        Owner(name="Fiona Kinya", contact="0767890123", location="Mombasa"),
        Owner(name="Grace kariuki", contact="0778901234", location="Kisumu"),
        Owner(name="Harry Maguire", contact="0789012345", location="Nakuru")
]

vet = [Vet(name="Dr. Rose", clinic="Happy Paws Vet", contact="0734567890",location="Westlands, Nairobi"),
    Vet(name="Dr. Brown", clinic="Healthy Pets Clinic", contact="0745678901",location="Kilimani, Nairobi"),
    Vet(name="Dr. Barasa", clinic="Paws and Claws Vet", contact="0756789012",location="Karen, Nairobi"),
    Vet(name="Dr. Evans", clinic="Pet Health Center", contact="0767890123",location="Langata, Nairobi"),
    Vet(name="Dr. Akello", clinic="Vet Care Clinic", contact="0778901234",location="Runda, Nairobi"),
    Vet(name="Dr. George", clinic="Animal Wellness Vet", contact="0789012345",location="Mombasa"),
    Vet(name="Dr. Chepkirui", clinic="Pet Harmony Clinic", contact="0790123456",location="Kisumu"),
    Vet(name="Dr. Juma", clinic="Furry Friends Vet", contact="0701234567",location="Nakuru"),
    Vet(name="Dr. Kimani", clinic="Pet Haven Clinic", contact="0712345678",location="Eldoret"),
    Vet(name="Dr. Joan", clinic="Vet Solutions Clinic", contact="0723456789",location="Meru")
]
rescue = [RescueCenter(name="Hope Rescue", location="Nairobi", contact="0711122233"),
    RescueCenter(name="Safe Haven Rescue", location="Mombasa", contact="0722233344"),
    RescueCenter(name="Animal Shelter", location="Kisumu", contact="0733344455"),
    RescueCenter(name="Rescue Paws", location="Nakuru", contact="0744455566"),
    RescueCenter(name="Pet Rescue", location="Eldoret", contact="0755566677"),
    RescueCenter(name="Wildlife Rescue", location="Meru", contact="0766677788"),
    RescueCenter(name="Animal Aid", location="Nairobi", contact="0777788899"),
    RescueCenter(name="Rescue Center", location="Mombasa", contact="0788899900"),
    RescueCenter(name="Pet Refuge", location="Kisumu", contact="0799900011"),
    RescueCenter(name="Animal Rescue", location="Nakuru", contact="0700112233")
]
dog = [Dog(name="Bruno", breed="German Shepherd", age="3 years", gender="Male", purpose="adoption", location="Kisumu", owner_id=1, vet_id=1, rescue_center_id=1),
    Dog(name="Buddy", breed="Labrador", age="2 years", gender="Male", purpose="adoption", location="Nairobi", owner_id=2, vet_id=2, rescue_center_id=2),
    Dog(name="Charlie", breed="Poodle", age="1 year", gender="Male", purpose="adoption", location="Kisumu", owner_id=3, vet_id=3, rescue_center_id=3),
    Dog(name="Daisy", breed="Beagle", age="4 months", gender="Female", purpose="adoption", location="Nakuru", owner_id=4, vet_id=4, rescue_center_id=4),
    Dog(name="Max", breed="Bulldog", age="3 months", gender="Male", purpose="adoption", location="Meru", owner_id=5, vet_id=5, rescue_center_id=5),
    Dog(name="Luna", breed="Golden Retriever", age="2 years", gender="Female", purpose="adoption", location="Eldoret", owner_id=6, vet_id=6, rescue_center_id=6),
    Dog(name="Bosco", breed="Rottweiler", age="1 year", gender="Male", purpose="adoption", location="Nairobi", owner_id=7, vet_id=7, rescue_center_id=7),
    Dog(name="Bella", breed="Pomeranian", age="6 months", gender="Female", purpose="adoption", location="Mombasa", owner_id=8, vet_id=8, rescue_center_id=8),
    Dog(name="Cooper", breed="Dachshund", age="1 year", gender="Male", purpose="adoption", location="Kisumu", owner_id=9, vet_id=9, rescue_center_id=9),
    Dog(name="Sadie", breed="Boxer", age="2 years", gender="Female", purpose="adoption", location="Nakuru", owner_id=10, vet_id=10, rescue_center_id=10)
]
# appt1 = Appointment(date=datetime(2025, 6, 10, 10, 30),reason="Annual vaccination",dog=dog,vet=vet)
# appointment = []
# for i in range(1, 11):
#     appointment_date = datetime(2025, 6, 10, 10, 30) + timedelta(days=i)
#     appt = Appointment(date=appointment_date, reason="Annual vaccination", dog_id=i, vet_id=i)
#     appointment.append(appt)


session.add_all(owner)
session.add_all(vet)
session.add_all(rescue)
session.add_all(dog)
# session.add_all(appointment)
session.commit()
print("Database seeded!")
