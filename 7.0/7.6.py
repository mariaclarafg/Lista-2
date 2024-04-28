import shutil

def copy_file_with_extension(file_name):
    try:
        
        base_name, extension = file_name.rsplit('.', 1)
        
        
        new_file_name = f"{base_name}.copy"
        
        shutil.copyfile(file_name, new_file_name)
        
        with open(new_file_name, 'r') as new_file:
            content = new_file.read()
        
        print("Copied content:")
        print(content)
    except FileNotFoundError:
        print("File not found.")
        
file_name = input("Enter the name of the file: ")

copy_file_with_extension(file_name)