from contact import Contact
from data_manager import DataManager
def main():
    data_manager = DataManager()
    
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            data_manager.add_contact(contact)

        elif choice == '2':
            for c in data_manager.contacts:
                print(f"Name: {c['name']}, Phone: {c['phone']}")

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            results = data_manager.search_contact(search_term)
            for c in results:
                print(f"\n{c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}")

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            new_contact = Contact(new_name, new_phone, new_email, new_address)
            data_manager.update_contact(name, new_contact)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            data_manager.delete_contact(name)

        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
