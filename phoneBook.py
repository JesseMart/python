"""PHONEBOOK APP"""

phone_Book = {"Jesse" : "123-456-7890"}
select_ion = 0

def phoneBook_menu():
    print("Electronic Phone Book")
    print("======================")
    print("1. Look up an entry")
    print("2. Set an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Quit")

phoneBook_menu()
while select_ion != 5:
    select_ion = int(input("Enter your selection (1-5): "))
    if select_ion == 1: 
        entry = input("Enter the name you're looking for: ")
        if entry in phone_Book:
            print("Name: ", entry, "\nPhone Number: ", phone_Book[entry])
        else:
            print("Name was not found!")
        print()
    elif select_ion == 2:
        print("++++ Add a new entry ++++")
        entry = input("Name: ")
        phone = input("Phone Number: ")
        phone_Book[entry] = phone
    elif select_ion == 3:
        print("++++ Remove an entry ++++")
        name = input("Enter name you would like to delete: ")
        if name in phone_Book:
            del phone_Book[name]
        else: 
            print("Name was not found")
        print ("Entry was deleted")
    elif select_ion == 4:
        print("+++++ List all entries ++++\n")
        for name in phone_Book:
            print("Name: ", name, "\nPhone Number: ", phone_Book[name])
        print()
    elif select_ion != 5:
        phoneBook_menu()
