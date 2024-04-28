class CustomError(Exception):
    def __init__(self, message="An error occurred."):
        self.message = message
        super().__init__(self.message)

def my_function(value):
    if value < 0:
        raise CustomError("The value canot be negative")
    else:
        result = 10 / value
        return result

try:
    number = int(input("Enter a positive integer number : "))
    final_result = my_function(number)
    print(f"Final result: {final_result:.2f}")
except CustomError as ce:
    print(f"Custom Error: {ce}")
except Exception as e:
    print(f"Generic Error: {e}")
