import os

def rename_file(file_name):
    try:
        base_name, extension = os.path.splitext(file_name)
        new_file_name = f"{base_name}_renomeado{extension}"
        os.rename(file_name, new_file_name)
        print(f"File renamed to: {new_file_name}")
    except FileNotFoundError:
        print("File not found.")

file_name = input("Enter the name of the file: ")

rename_file(file_name)