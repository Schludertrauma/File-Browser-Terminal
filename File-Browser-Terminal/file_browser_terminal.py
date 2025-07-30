'''File Browser Terminal'''
'''This module provides a terminal interface for browsing files and directories.'''
'''It allows users to navigate through the file system, view files, and execute commands like opening, editing, creating, and deleting files.'''


# Library and Module Imports

import os
import time

# File Browser Terminal Class


class file_browser_terminal:
    def welcome(self):
        # Welcome message for the terminal
        print("Welcome to the File Browser Terminal!")
        print("You can navigate through your file system and perform various operations.")
        print("Type 'help' to see available commands.")
        print()
        time.sleep(1)

    def choose_directory_on_startup(self):
        # Allow user to choose a directory on startup
        initial_directory = input("Enter the directory you want to start in: ")
        print()
        try:
            os.chdir(initial_directory)
        except FileNotFoundError:
            print(
                f"Directory '{initial_directory}' not found. Using current directory.")
            print()
            time.sleep(1)

    def menu(self):
        # Display the menu options for the terminal
        print("File Browser Terminal Menu:")
        print("1. Change Directory")
        print("2. List Files")
        print("3. Open File")
        print("4. Edit File")
        print("5. Create File")
        print("6. Delete File")
        print("7. Exit")

    def change_directory(self, directory):
        # Change the current working directory
        try:
            os.chdir(directory)
            print(f"Changed directory to: {os.getcwd()}")
            print()
        except FileNotFoundError:
            print(f"Directory '{directory}' not found.")
            print()
            time.sleep(1)
        except Exception as e:
            print(f"Error changing directory: {e}")
            print()
            time.sleep(1)

    def list_files(self):
        # List files in the current directory
        try:
            files = os.listdir()
            print("Files in current directory:")
            print()
            time.sleep(1)
            for file in files:
                print(file)
                print()
            time.sleep(1)
        except Exception as e:
            print(f"Error listing files: {e}")
            print()
            time.sleep(1)

    def open_file(self, filename):
        # Open a file and display its contents
        try:
            if os.path.isfile(filename):
                with open(filename, 'r') as file:
                    content = file.read()
                    print(f"Content of {filename}:\n{content}")
            else:
                print(f"File '{filename}' does not exist.")
            print()
            time.sleep(1)
        except Exception as e:
            print(f"Error opening file: {e}")
            print()
            time.sleep(1)

    def edit_file(self, filename):
        # Edit a file by appending content to it
        try:
            if os.path.isfile(filename):
                with open(filename, 'a') as file:
                    content = input("Enter content to append to the file: ")
                    print()
                    time.sleep(1)
                    file.write(content + '\n')
                    print(f"Content appended to {filename}.")
                print()
                time.sleep(1)
            else:
                print(f"File '{filename}' does not exist.")
                print()
                time.sleep(1)
        except Exception as e:
            print(f"Error editing file: {e}")
            print()
            time.sleep(1)

    def create_file(self, filename):
        # Create a new file
        try:
            with open(filename, 'w') as file:
                print(f"File '{filename}' created successfully.")
            print()
            time.sleep(1)
        except Exception as e:
            print(f"Error creating file: {e}")
            print()
            time.sleep(1)

    def delete_file(self, filename):
        # Delete a file
        try:
            if os.path.isfile(filename):
                os.remove(filename)
                print(f"File '{filename}' deleted successfully.")
                print()
                time.sleep(1)
            else:
                print(f"File '{filename}' does not exist.")
                print()
                time.sleep(1)
        except Exception as e:
            print(f"Error deleting file: {e}")
            print()
            time.sleep(1)

    def exit_terminal(self):
        # Exit the terminal
        print("Exiting File Browser Terminal. Goodbye!")
        time.sleep(1)
        exit()

    def main(self):
        # Main function to run the terminal
        self.welcome()
        self.choose_directory_on_startup()
        while True:
            self.menu()
            print()
            choice = input("Enter your choice: ")
            if choice == '1':
                directory = input("Enter directory path: ")
                print()
                self.change_directory(directory)
            elif choice == '2':
                self.list_files()
            elif choice == '3':
                filename = input("Enter filename to open: ")
                print()
                self.open_file(filename)
            elif choice == '4':
                filename = input("Enter filename to edit: ")
                print()
                self.edit_file(filename)
            elif choice == '5':
                filename = input("Enter filename to create: ")
                print()
                self.create_file(filename)
            elif choice == '6':
                filename = input("Enter filename to delete: ")
                print()
                self.delete_file(filename)
            elif choice == '7':
                self.exit_terminal()
            else:
                print("Invalid choice. Please try again.")


# Main execution block

if __name__ == "__main__":
    # Create an instance of the file_browser_terminal class and run the main function
    terminal = file_browser_terminal()
    terminal.main()
