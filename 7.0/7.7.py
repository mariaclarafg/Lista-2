import os

def create_temp_directory():
    try:
        os.mkdir("temp")
        
        os.chdir("temp")
        
        with open("temp.txt", "w") as file:
            file.write("This is a temp file.")
        
        print("Directory 'temp' and file 'temp.txt' created successfully.")
    except FileExistsError:
        print("Directory 'temp' already exists.")

create_temp_directory()