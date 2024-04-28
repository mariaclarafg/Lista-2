def read_integers_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            numbers = [int(line.strip()) for line in file.readlines()]
            return numbers
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except ValueError:
        print(f"Error: Invalid data found in '{file_name}'. Please make sure there's onlu integers numbers in the file")
    except Exception as e:
        print(f"An error occurred while reading '{file_name}': {e}")

def calculate_sum(numbers):
    return sum(numbers) if numbers else 0

file_name = input("Enter the file name: ")

numbers_list = read_integers_from_file(file_name)
if numbers_list is not None:
    total_sum = calculate_sum(numbers_list)
    print(f"The sum of the numbers in '{file_name}' is: {total_sum}")
else:
    print("Stoped program due to an error.")
