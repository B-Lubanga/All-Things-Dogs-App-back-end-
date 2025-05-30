from models.dog import Dog
from models.owner import Owner
from models.vet import Vet
from models.appointment import Appointment
from models.rescue_center import RescueCenter
from database import db_session
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def menu():
    while True:
        print("\n🐶 DOG ADOPTION CLI")
        print("1. Register a Dog")
        print("2. Search Dogs by Breed and Location")
        print("3. Assign Vet to a Dog")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_dog()
        elif choice == '2':
            search_dogs()
        elif choice == '3':
            assign_vet()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

def add_dog():
    name = input("Dog's name: ")
    breed = input("Breed: ")
    location = input("Location: ")
    purpose = input("Purpose (adoption/rescue/sale): ")

    # Add owner details
    owner_name = input("Owner's name: ")
    contact = input("Owner's contact: ")
    owner_location = input("Owner's location: ")

    session = db_session()

    # Create and save the owner first
    owner = Owner(name=owner_name, contact=contact, location=owner_location)
    session.add(owner)
    session.commit()

    # Now create the dog and assign the owner
    dog = Dog(name=name, breed=breed, location=location, purpose=purpose)
    session = db_session()
    session.add(dog)
    session.commit()
    print(f"✅ Dog '{name}' added successfully!")

def search_dogs():
    breed = input("Enter breed to search: ")
    location = input("Enter location: ")
  
    session = db_session()
    dogs = session.query(Dog).filter(Dog.breed.like(f"%{breed}%"), Dog.location.like(f"%{location}%")).all()
    
    if dogs:
        print("\n📋 Matching Dogs:")
        for dog in dogs:
            print(f"- {dog.name} ({dog.breed}) in {dog.location} | Purpose: {dog.purpose}")
    else:
        print("No dogs found with that breed and location.")

def assign_vet():
    dog_id = input("Enter Dog ID to assign vet: ")
    vet_id = input("Enter Vet ID: ")

    session = db_session()
    dog = session.get(Dog, dog_id)
    vet = session.get(Vet, vet_id)

    if dog and vet:
        dog.vet = vet
        session.commit()
        print(f"✅ Assigned Vet {vet.name} to Dog {dog.name}")
    else:
        print("❌ Invalid dog or vet ID.")

if __name__ == '__main__':
    menu()
