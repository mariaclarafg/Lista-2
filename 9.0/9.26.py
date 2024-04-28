def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        raise ValueError("The number cannot divide by zero")

def add_numbers(x, y):
    return x + y

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result_division = divide_numbers(num1, num2)
    print(f"Division's result: {result_division}")

    result_addition = add_numbers(num1, num2)
    print(f"Addition result: {result_addition}")

except ValueError as ve:
    print(f"Value Error: {ve}")
except Exception as e:
    print(f"An error occurred: {e}")
