import os

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' has been deleted.")
    except FileNotFoundError:
        print("File not found.")

file_name = input("Enter the name of the file to delete: ")

delete_file(file_name)