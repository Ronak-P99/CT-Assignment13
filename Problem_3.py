'''
3. Mastering Python Modules and Aliases
Objective:
The aim of this assignment is to enhance your proficiency in using Python modules, both standard and custom, 
with a specific focus on importing with aliases. This will develop your skills in organizing code, simplifying access to module components, 
and effectively managing namespace in Python programs.

Task 1: Custom Module with Aliases

Problem Statement: Create a custom module named text_utils.py with functions for string manipulation 
(e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions.
'''

import text_utils


def main():
    while True:
        print("\n1. Capitalize word\n2. Reverse a word\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            user_string = input("Now choose a string ")
            text_utils.capitalize_string(user_string)
        elif choice == '2':
            user_string = input("Now choose a string ")
            text_utils.reverse_string(user_string)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()