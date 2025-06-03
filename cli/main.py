from models.dog import Dog
from models.owner import Owner
from models.vet import Vet
from models.rescue_center import RescueCenter
from database import db_session, engine, Base, create_tables

Base.metadata.create_all(engine)
create_tables()


def menu():
    while True:
        print("\n🐶 DOG ADOPTION CLI")
        print("1. Register a Dog")
        print("2. Search Dogs by Breed and Location")
        print("3. Assign Vet to a Dog")
        print("4. List All Dogs")
        print("5. List All Vets")
        print("6. List All Rescue Centers")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_dog()
        elif choice == '2':
            search_dogs()
        elif choice == '3':
            assign_vet()
        elif choice == '4':
            list_dogs()
        elif choice == '5':
            list_vets()
        elif choice == '6':
            list_rescue_centers()
        elif choice == '7':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid option. Please try again.")


# ---------- Add Dog with Owner, Vet, Rescue Center ----------
def add_dog():
    session = db_session()

    print("\n🐾 Registering New Dog")
    name = input("Dog's name: ")
    breed = input("Breed: ")
    location = input("Location: ")
    age = input("Age: ")
    gender = input("Gender: ")
    purpose = input("Purpose (adoption/rescue/sale): ")

    # --- Owner Section ---
    owner_query = input("Enter part of owner's name to search or type 'new': ")
    if owner_query.lower() == "new":
        owner_name = input("Owner's name: ")
        contact = input("Owner's contact: ")
        owner_location = input("Owner's location: ")
        owner = Owner(name=owner_name, contact=contact, location=owner_location)
        session.add(owner)
        session.commit()
    else:
        owners = session.query(Owner).filter(Owner.name.ilike(f"%{owner_query}%")).all()
        if not owners:
            print("❌ No matching owners found.")
            return
        print("\nMatching Owners:")
        for idx, o in enumerate(owners):
            print(f"{idx + 1}. {o.name} - {o.contact} - {o.location}")
        choice = int(input("Choose owner by number: ")) - 1
        owner = owners[choice]

    # --- Vet Section ---
    vet = choose_from_search(session, Vet, "name", ["name", "specialty"], "Vet")

    # --- Rescue Center Section ---
    rescue_center = choose_from_search(session, RescueCenter, "name", ["name", "location"], "Rescue Center")

    # --- Save Dog ---
    dog = Dog(
        name=name,
        breed=breed,
        location=location,
        age=age,
        gender=gender,
        purpose=purpose,
        owner=owner,
        vet=vet,
        rescue_center=rescue_center
    )

    session.add(dog)
    session.commit()
    print(f"✅ Dog '{name}' registered successfully!")


# ---------- Helper: Choose from Model by Name ----------
def choose_from_search(session, model, field, display_fields, label):
    query = input(f"Enter part of {label}'s name (or leave blank to skip): ")
    if not query:
        return None
    results = session.query(model).filter(getattr(model, field).ilike(f"%{query}%")).all()
    if not results:
        print(f"❌ No matching {label}s found.")
        return None

    print(f"\nMatching {label}s:")
    for idx, item in enumerate(results):
        info = " - ".join([str(getattr(item, f)) for f in display_fields])
        print(f"{idx + 1}. {info}")
    try:
        choice = int(input(f"Choose {label} by number: ")) - 1
        return results[choice] if 0 <= choice < len(results) else None
    except:
        print("❌ Invalid input.")
        return None


# ---------- Search Dogs ----------
def search_dogs():
    breed = input("Enter breed to search (or leave blank): ").strip()
    location = input("Enter location to search (or leave blank): ").strip()

    session = db_session()

    query = session.query(Dog)

    # Add filters only if inputs are provided
    if breed:
        query = query.filter(Dog.breed.ilike(f"%{breed}%"))
    if location:
        query = query.filter(Dog.location.ilike(f"%{location}%"))

    dogs = query.all()

    if dogs:
        print("\n📋 Matching Dogs:")
        for dog in dogs:
            print(f"- {dog.name} ({dog.breed}) in {dog.location} | Purpose: {dog.purpose}")
    else:
        print("❌ No dogs found matching your criteria.")


# ---------- Assign Vet ----------
def assign_vet():
    session = db_session()
    dog_name = input("Enter dog name to assign vet: ")
    dog = session.query(Dog).filter(Dog.name.ilike(f"%{dog_name}%")).first()
    if not dog:
        print("❌ Dog not found.")
        return

    vet = choose_from_search(session, Vet, "name", ["name", "specialty"], "Vet")
    if vet:
        dog.vet = vet
        session.commit()
        print(f"✅ Assigned Vet '{vet.name}' to Dog '{dog.name}'")


# ---------- List All Data ----------
def list_dogs():
    session = db_session()
    dogs = session.query(Dog).all()
    if not dogs:
        print("📭 No dogs registered yet.")
        return
    print("\n🐶 All Registered Dogs:")
    for d in dogs:
        owner_info = f"{d.owner.name}" if d.owner else "None"
        vet_info = f"{d.vet.name}" if d.vet else "None"
        rc_info = f"{d.rescue_center.name}" if d.rescue_center else "None"
        print(f"- {d.name} | {d.breed} | {d.location} | Owner: {owner_info} | Vet: {vet_info} | RC: {rc_info}")


def list_vets():
    session = db_session()
    vets = session.query(Vet).all()
    if not vets:
        print("📭 No vets available.")
        return
    print("\n🩺 Vet Clinics:")
    for v in vets:
        print(f"- {v.name} | Location: {v.location}")


def list_rescue_centers():
    session = db_session()
    centers = session.query(RescueCenter).all()
    if not centers:
        print("📭 No rescue centers found.")
        return
    print("\n🏡 Rescue Centers:")
    for rc in centers:
        print(f"- {rc.name} | Location: {rc.location}")


if __name__ == '__main__':
    menu()
