import math

while True:
    try:
        num = int(input("Enter an integer number: "))
        if num < 0:
            raise ValueError("Please enter a positive number")
        else:
            result = math.sqrt(num)
            print(f"The square root of {num} is {result:.2f}")
            break
    except ValueError as e:
        print(e)
