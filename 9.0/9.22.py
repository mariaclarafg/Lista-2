class EmptyListError(Exception):
    def __init__(self, message="The list is empty.The average can't be calculeted"):
        self.message = message
        super().__init__(self.message)

def calculate_average(numbers):
    if not numbers:
        raise EmptyListError()
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

try:
    numbers_list = [10, 20, 30, 40, 50]
    avg = calculate_average(numbers_list)
    print(f"Average: {avg}")
    
    empty_list = []
    avg_empty = calculate_average(empty_list)
except EmptyListError as e:
    print(e)
except Exception as ex:
    print(f"Error: {ex}")
