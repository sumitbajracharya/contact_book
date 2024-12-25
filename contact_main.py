from controller import DatabaseManager

print ("-------------------------------------------------------------------")
print ("Welcome to TC Contact Book")
print ("-------------------------------------------------------------------")

print ("Please choose your action :")
print ("1. Add a new contact")
print ("2. View all contacts")
print ("3. Search a contact")
print ("4. Update a contact")
print ("5. Delete a contact")
print ("6. Search contact by ID")
print ("7. Exit")

choice = int(input("Enter your choice: "))

# For DB
host = "localhost"
user = "root"
password = ""
database = "phonebook"

db_manager = DatabaseManager(host, user, password, database)

if choice == 1:
    print ("Add a new contact")   
    name = input("Enter name: ")
    phone = int(input("Enter phone: "))

    db_manager.add_person(name, phone)

elif choice == 2:
    print ("View all contacts")
    db_manager.list_persons()
elif choice == 3:  
    print ("Search a contact")
elif choice == 4:
    print ("Update a contact")
elif choice == 5:
    print ("Delete a contact")
    Id = input ("please enter ID of contact to delete: ")
    db_manager.delete_person(Id)
elif choice == 6:
    print ("Search contact by ID: ")
    Id = input ("please enter ID of contact: ")
    db_manager.search_person(Id)
elif choice == 7:
    print ("Exit")
else:
    print ("Invalid choice")