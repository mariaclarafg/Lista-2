def count_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            line_count = sum(1 for line in file)
            print("Number of lines in the file:", line_count)
    except FileNotFoundError:
        print("File not found.")

file_name = input("Enter the name of the text file: ")

count_lines(file_name)