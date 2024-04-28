def display_file_content():
    file_name = input("Enter the name of the file: ")
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found.")