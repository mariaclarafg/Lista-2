def read_file_contents(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found. Try again.")
    except Exception as e:
        print(f"An error occurred while opening '{file_name}': {e}")

while True:
    file_name = input("Enter the file name: ")
    file_contents = read_file_contents(file_name)
    
    if file_contents is not None:
        print(f"Contents of '{file_name}':{file_contents}")
        break
