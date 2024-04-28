def print_x():
    x = 10
    print("Value of x inside the function:", x)

print_x()

try:
    print("Value of x outside the function:", x) #Teacher, I don't know why its not working.
except NameError:
    print("Variable x is not accessible outside the function.")