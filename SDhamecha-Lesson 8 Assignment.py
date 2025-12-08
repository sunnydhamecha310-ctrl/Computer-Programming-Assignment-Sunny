#names = ["sunny", "sam", "vicky"]

#with open ("my_file.txt","a") as file:
#    for name in names:
#        file.write(name + "\n")
names = "contacts.txt"

def write_contacts(contacts):
    with open(names, "w") as file:
        i = 0
        while i < len(contacts):
            contacts = contacts[i]
            file.write(f"{contacts}\n")
            i = i + 1

def read_contacts():
    contacts = []
    try:
        with open(names, "r") as file:
            for line in file:
                line = line.replace("\n", "") 
                contacts.append(line)
    except FileNotFoundError:
        pass
    return contacts

def create_file():
    try:
        write_contacts([])
        print(f"File '{names}' created successfully.")
    except Exception:
        print(f"Error creating file '{names}'.")
    print()

def add_new_contact(contacts):
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    email = input("Enter email address: ")
    
    new_contact_string = f"{name}, {number}, {email}"
    contacts.append(new_contact_string)
    
    print(f"Contact added successfully!\n")

def view_all_contacts(contacts):
    if len(contacts) == 0:
        print("There are no contacts to view.")
    else:
        print("\n Current Contacts")
        i = 0
        while i < len(contacts):
            contact_number = i + 1
            contact_data = contacts[i]
            print(f"{contact_number}. {contact_data}")
            i = i + 1
        print("------------------------")

def modify_contact(contacts):
    
    view_all_contacts(contacts)
    
    
    if len(contacts) == 0:
        return

    try:
        selection = input("Enter number of contact to modify: ")
        index_to_modify = int(selection)
        
        if 1 <= index_to_modify <= len(contacts):
            list_index = index_to_modify - 1
            
            old_contact_string = contacts[list_index]
            print(f"\n Modifying Contact {index_to_modify} ")
            print(f"Current: {old_contact_string}")
            
           
            print("\nPlease enter the full new contact details:")
            new_name = input("Enter new Name: ")
            new_number = input("Enter new Number: ")
            new_email = input("Enter new Email: ")
            
           
            new_contact_string = f"{new_name}, {new_number}, {new_email}"
            contacts[list_index] = new_contact_string
            
            print(f"\nContact {index_to_modify} successfully modified.\n")
        else:
            print("Invalid contact number.\n")
            
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def save_and_exit(contacts):
    write_contacts(contacts)
    print("All changes saved.")
    print("Thank you!")
    print("Completed by Shivang Dhamecha")

def display_menu():
    print("Welcome to the Contact Manager App")
    print("Please select one of the following options to perform the corresponding action:")
    print("1. Create new contact file.")
    print("2. Add new contact.")
    print("3. View all contacts.")
    print("4. Modify an existing contact.")
    print("5. Save and Exit.")
    print("-" * 25)

def main():
    
    display_menu() 
    contacts = read_contacts()
    
    while True:
        command = input("Enter your choice (1-5): ")
        
        if command == "1":
            create_file()
        elif command == "2":
            add_new_contact(contacts)
        elif command == "3":
            view_all_contacts(contacts)
        elif command == "4":
            modify_contact(contacts)
        elif command == "5":
            save_and_exit(contacts)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")
            
        if command != "5":
             display_menu()

if __name__ == "__main__":
    main()