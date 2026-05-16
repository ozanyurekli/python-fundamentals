import json

try:
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = {}

while True:

    print("""
    --- Contact Book ---
    1. Add Contact
    2. Search Contact
    3. Delete Contact
    4. List All Contacts
    5. Quit
    """)    

    choice =  int(input("\nChoose an Option: "))

    if choice == 5:
        print("Goodbye")

        with open("contacts.json", "w") as f:
            json.dump(contacts, f)
            
        break

    elif choice == 1:
        name = input("Enter a name: ") 
        phoneNumber = input("Enter a phone number: ") 

        contacts[name] = phoneNumber

        print("Contact Saved\n")

    
    elif choice == 4:
        if not contacts:
            print("Contacts is Empty")
        else:
            for name, phone in contacts.items():
                print(f"{name} - {phone}")

    elif choice == 2:
        searched_name = input("Enter a name to search: ")
        if searched_name in contacts:
            print(f"{searched_name} — {contacts[searched_name]}")        
        else:
            print("No contact found")

    elif choice == 3:
        delete_contact = input("Enter a name to delete: ")
        if delete_contact in contacts:
            del contacts[delete_contact]
            print("Contact Deleted")
        else:
            print("Contact not found!")

    else:
        print(f"You Chose {choice}\n")