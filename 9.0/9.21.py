try:
    file_name = input("Enter the file name: ")
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found, make sure the file exists and try again.")
except Exception as e:
    print(f"error: {e}")
