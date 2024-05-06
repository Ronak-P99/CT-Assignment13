'''
2. Exploring Python Modules and Data Structures Assignment
Objective:
The aim of this assignment is to deepen your understanding of Python modules, 
both built-in and custom, and to enhance your skills in working with various Python data structures like lists, dictionaries, and sets. 
This assignment focuses on practical applications of these concepts in real-world scenarios.

Task 1: Contact List Manager

Problem Statement: Create a Python script using a custom module to manage a contact list. The script should allow adding, 
removing, and displaying contacts stored in a list.'''

import contacts_portal

def main():
    contacts = []
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Delete Contact\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter phone: ")
            email = input("Enter Email: ")
            contacts_portal.add_contact(contacts, name, phone, email)
        elif choice == '2':
            contacts_portal.view_contact(contacts)
        elif choice == '3':
            name = input("Enter Name to Delete: ")
            if contacts_portal.delete_contact(contacts, name) is not None:
                print("Contact deleted.")
            else:
                print("Contact not found")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()