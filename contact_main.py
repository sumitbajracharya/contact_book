
print ("-------------------------------------------------------------------")
print ("Welcome to TC Contact Book")
print ("-------------------------------------------------------------------")

print ("Please choose your action :")
print ("1. Add a new contact")
print ("2. View all contacts")
print ("3. Search a contact")
print ("4. Update a contact")
print ("5. Delete a contact")
print ("6. Exit")

choice = int(input("Enter your choice: "))


if choice == 1:
    print ("Add a new contact")    
elif choice == 2:
    print ("View all contacts")
elif choice == 3:  
    print ("Search a contact")
elif choice == 4:
    print ("Update a contact")
elif choice == 5:
    print ("Delete a contact")
elif choice == 6:
    print ("Exit")
else:
    print ("Invalid choice")